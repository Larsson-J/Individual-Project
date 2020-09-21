import os
import glob
import pandas as pd

# making my working directory

os.chdir(r"C:\Users\Johan Larsson\PycharmProjects\Application\data")

# matching the patten 'csv', saving them in a list called all_filenames

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

# combining all the csv files and saving them into a new .csv file

combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')