import pandas as pd

import matplotlib.pyplot as plt

def histogram_sleep(path):
    print(path)
    # print(data)
    # print(type(data))
    # print(data['type'][0])
    # print(type(data['type'][0]))
    # print(data['levels'][0])
    pass

def histogram_minutesAwake(data):
    #columns = data.columns
    #minutesAsleep = data['minutesAsleep']
    #print(f'minutesAsleep = {minutesAsleep}')
    #print(minutesAsleep)
    #print(minutesAsleep[0])
    #print(type(minutesAsleep))
    data.hist(bins=20)
    plt.show()

def print_columns(data):
    columns = data.columns
    print(f'columns[0]: {columns[0]}, len(columns) = {len(columns)}')
    print(columns)
    for column in columns:
        #print(type(column))
        print(column)
    print(column)

def main():
    print('In main')
    path = './data/Me/user-site-export/sleep-2017-08-11.json'
    data = pd.read_json(path)
    #histogram_sleep(path)
    #print_columns(data)
    histogram_minutesAwake(data)

if __name__ == '__main__':
    print("Start")
    main()
    print('Done\a')
