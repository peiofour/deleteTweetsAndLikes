#!/usr/bin/env python

# Made by Pierre Fournier

import argparse
import twitter
import csv
import sys
import time
import os
from dateutil.parser import parse


def delete_like(api, date, r):
    with open("likes.csv") as file:
        count = 0

        for row in csv.DictReader(file):
            tweet_id = int(row["tweet_id"])

            try:
                print("Deleting like")
                api.CreateFavorite(status_id=tweet_id)
                api.DestroyFavorite(status_id=tweet_id)
                print(tweet_id)
                print(count)
                count += 1
                time.sleep(0.7)

            except twitter.TwitterError as err:
                print("Exception: %s\n" % err.message)

    print("Number of disliked tweets: %s\n" % count)


def delete_tweet(api, date, r):
    with open("tweets.csv") as file:
        count = 0

        for row in csv.DictReader(file):
            tweet_id = int[row("tweet_id")]
            tweet_date = parse(row("timestamp"), ignoretz=True).date()

            if date != "" and tweet_date >= parse(date).date():
                continue

            if r == "retweet" and row["retweet_status_id"] == "" or r == "reply" and row["in_reply_to_status_id"] == "":
                continue

            try:
                print("Deleting tweet #(0)")

                api.DestroyStatus(tweet_id)
                count += 1
                time.sleep(0.5)

            except twitter.TwitterError as err:
                print("Exception %s\n" % err.message)

    print("Number of deleted tweets : %s\n" % count)


def error(message, exit_code=1):
    sys.stderr.write("Error %s\n" % message)
    exit(exit_code)

