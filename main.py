from cassandra.cluster import Cluster

cluster = Cluster(contact_points=['localhost'])
session = cluster.connect('killrvideo')
records = session.execute("SELECT * FROM videos_by_tag_year")

for r in records:
    print(r[0], r[1], r[2], r[3], r[4])