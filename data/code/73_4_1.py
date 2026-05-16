def time_difference(ts1, ts2):
    return abs(ts1 - ts2)
if __name__ == '__main__':
    time1 = 1678886400
    time2 = 1678972800
    difference = time_difference(time1, time2)
    print(difference)