# open artists.csv, turn it into a dictionary with third column as key and first column as value
import os
import csv

out_dir = "wildcards"
with open('artists.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    headers = next(reader)
    artists = {}
    all_artist_names = []
    for row in reader:
        all_artist_names.append(row[0])
        if row[2] in artists:
            artists[row[2]].append(row[0])
        else:
            artists[row[2]] = [row[0]]

# check if folder exists, if not create it
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

def write_to_file(filename, list):
    lines = list
    filename.writelines(s + '\n' for s in lines)

for key in artists:
    with open(f'{out_dir}/artist-{key}.txt', 'w', encoding='utf-8') as f:
        write_to_file(f, artists[key])

all_artist_names = set(all_artist_names)

with open(f'{out_dir}/artist-csv.txt', 'w', encoding='utf-8') as f:
    write_to_file(f, all_artist_names)