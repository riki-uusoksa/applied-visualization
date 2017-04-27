#University of Michigan (42.2780475, -83.7384128)
#West Bound (42.280717, -83.979402)
#North Bound (42.457713, -83.738632)
#East Bound (42.278488, -83.495771)
#South Bound (42.097174, -83.741057)

import os
import csv
import pandas as pd

#Set boundaries for subsetting
lat_low = 42.097174
lat_high = 42.457713
lon_low = -83.979402
lon_high = -83.495771

#Empty list to contain the filenames and an empty DataFrame to contain the results
fileList = []
severe_weather = pd.DataFrame()

#Get filenames to be iterated over in the next step
for i in os.listdir(os.getcwd()):
    if 'StormEvents' in i:
        fileList.append(i)

#Iterate through all the files and get results that fit in the vicinity of Ann Arbor
for idx, i in enumerate(fileList):
    print(idx)
    df = pd.read_csv(fileList[idx], encoding='latin-1', low_memory=False)
    df = df.query('((BEGIN_LAT >= @lat_low & BEGIN_LAT <= @lat_high) & (BEGIN_LON >= @lon_low & BEGIN_LON <= @lon_high))'
                  '|((END_LAT >= @lat_low & END_LAT <= @lat_high) & (END_LON >= @lon_low & END_LON <= @lon_high))')
    severe_weather = severe_weather.append(df, ignore_index=True)
    df = None

#Write to csv file to be used
severe_weather.to_csv('severe_weather.csv', index=False)