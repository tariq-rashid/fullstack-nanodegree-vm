# "Database code" for the DB Forum.

import datetime
import psycopg2, bleach

#POSTS = [("This is the first post.", datetime.datetime.now())]
#db = psycopg2.connect("dbname=forum")


def get_posts():
  db = psycopg2.connect("dbname=forum")
  c = db.cursor()
  query = "select content, time from posts order by time desc"
  c.execute(query)
  posts = c.fetchall()
  db.close
  return posts

def add_post(content):
  db = psycopg2.connect("dbname=forum")
  c = db.cursor()
  timestamp = datetime.datetime.now()
  #query = "insert into posts values (content , timestamp) "
  c.execute("insert into posts values (%s)" , (bleach.clean(content),))
  db.commit()
  db.close
  


