import yaml
import tweepy
import json

auth = tweepy.OAuthHandler("wDbUd48WMU44dwV8fobfXTo3K", "cYJifzfQfdftwpqUIrNXTo9sImIpxOsIWXKG7SbvyDPX2oSy8l")
auth.set_access_token("1229058726-A3r6ZWBcUqqCGreUEixpsevUzWKPA6km2tSdY35", "fLugyek8MfKsuYSnrRDpaFuq46N1H3UNlG80JK58DyOi5")

api = tweepy.API(auth)


companies_file = yaml.load(open("companies.yaml").read())
companies = companies_file["companies"]

s_file = open("new_dumps.json", "a+")
s_file.write("{")


dump_file = open("new_dumps.yaml", "a+")
dump_dict = {}

limit = 160
current_calls = 0

for name in companies:
    if current_calls < limit:
        tweets = api.search("from:{}".format(name))
        dump_dict[name] = []
        for tweet in tweets:
            temp = "\"{}\": {}".format(name, json.dumps(tweet._json))
            dump_dict[name].append(tweet._json)
        current_calls += 1
    else:
        break

s_file.write(json.dumps(dump_dict))

dump_file.close()
s_file.close()
