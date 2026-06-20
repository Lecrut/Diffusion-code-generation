import datetime

def calculate_time_difference(dt1, dt2):
    if not isinstance(dt1, datetime.datetime) or not isinstance(dt2, datetime.datetime):
        raise ValueError("Both inputs must be instances of datetime.datetime")
    
    difference = dt2 - dt1
    return difference

if __name__ == '__main__':
    time1 = datetime.datetime(2023, 1, 1, 10, 0, 0)
    time2 = datetime.datetime(2023, 1, 1, 11, 0, 0)
    time3 = datetime.datetime(2023, 1, 1, 9, 0, 0)

    diff1 = calculate_time_difference(time1, time2)
    print(f"Difference between time1 and time2: {diff1}")

    try:
        diff2 = calculate_time_difference(time1, "not a datetime")
        print(f"Difference between time1 and 'not a datetime': {diff2}")
    except ValueError as e:
        print(e)

    diff3 = calculate_time_difference(time2, time1)
    print(f"Difference between time2 and time1: {diff3}")

    diff4 = calculate_time_difference(time1, time3)
    print(f"Difference between time1 and time3: {diff4}")