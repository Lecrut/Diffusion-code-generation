import datetime

def calculate_time_difference(dt1, dt2):
    difference = dt1 - dt2
    return difference

if __name__ == '__main__':
    time1 = datetime.datetime(2023, 4, 1, 12, 0, 0)
    time2 = datetime.datetime(2023, 4, 1, 13, 0, 0)
    time3 = datetime.datetime(2023, 3, 31, 12, 0, 0)
    
    diff1 = calculate_time_difference(time1, time2)
    print(f"Difference between time1 and time2: {diff1}")
    
    diff2 = calculate_time_difference(time2, time3)
    print(f"Difference between time2 and time3: {diff2}")