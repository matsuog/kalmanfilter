import matplotlib.pyplot as plt
import numpy as np
import csv

filename = './data/populationdata.csv'
with open(filename, encoding='utf8', newline='') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        print(row)
