from datetime import datetime
def calculate_time_difference(dt1, dt2):
    if dt1 is None or dt2 is None:
        raise ValueError("Both datetime objects must be provided.")
    return dt2 - dt1
if __name__ == '__main__':
    time1 = datetime(2023, 1, 1, 10, 0, 0)
    time2 = datetime(2023, 1, 3, 12, 30, 0)
    difference1 = calculate_time_difference(time1, time2)
    print(f"Difference between {time1} and {time2}: {difference1}")
    time3 = datetime(2023, 1, 10, 15, 0, 0)
    time4 = datetime(2023, 1, 10, 15, 0, 0)
    difference2 = calculate_time_difference(time3, time4)
    print(f"Difference between {time3} and {time4}: {difference2}")
    time5 = datetime(2023, 1, 5, 9, 0, 0)
    time6 = datetime(2023, 1, 1, 10, 0, 0)
    difference3 = calculate_time_difference(time5, time6)
    print(f"Difference between {time5} and {time6}: {difference3}")
    try:
        calculate_time_difference(time1, None)
    except ValueError as e:
        print(f"Caught expected error: {e}")