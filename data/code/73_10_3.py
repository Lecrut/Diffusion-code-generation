from datetime import datetime
def calculate_time_difference(dt1, dt2):
    if dt1 is None or dt2 is None:
        raise ValueError("Both datetime objects must be provided.")
    return dt2 - dt1
if __name__ == '__main__':
    time1 = datetime(2023, 1, 1, 10, 0, 0)
    time2 = datetime(2023, 1, 3, 14, 30, 0)
    difference = calculate_time_difference(time1, time2)
    print(f"Time 1: {time1}")
    print(f"Time 2: {time2}")
    print(f"Difference: {difference}")
    time3 = datetime(2023, 1, 1, 10, 0, 0)
    time4 = datetime(2023, 1, 1, 10, 0, 0)
    difference2 = calculate_time_difference(time3, time4)
    print(f"\nTime 3: {time3}")
    print(f"Time 4: {time4}")
    print(f"Difference (Same time): {difference2}")
    time5 = datetime(2023, 1, 1, 23, 59, 59)
    time6 = datetime(2023, 1, 2, 0, 0, 0)
    difference3 = calculate_time_difference(time5, time6)
    print(f"\nTime 5: {time5}")
    print(f"Time 6: {time6}")
    print(f"Difference (Crossing day): {difference3}")
    try:
        calculate_time_difference(time1, None)
    except ValueError as e:
        print(f"\nError handled: {e}")