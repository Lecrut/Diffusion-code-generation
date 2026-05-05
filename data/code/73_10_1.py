from datetime import datetime
def calculate_time_difference(dt1, dt2):
    if dt1 is None or dt2 is None:
        raise ValueError("Both datetime objects must be provided.")
    return dt2 - dt1
if __name__ == '__main__':
    time1 = datetime(2023, 1, 1, 10, 0, 0)
    time2 = datetime(2023, 1, 3, 14, 30, 15)
    difference = calculate_time_difference(time1, time2)
    print(difference)
    time3 = datetime(2024, 5, 1, 0, 0, 0)
    time4 = datetime(2024, 5, 1, 0, 0, 0)
    difference2 = calculate_time_difference(time3, time4)
    print(difference2)
    time5 = datetime(2023, 12, 31, 23, 59, 59)
    time6 = datetime(2024, 1, 1, 0, 0, 0)
    difference3 = calculate_time_difference(time5, time6)
    print(difference3)