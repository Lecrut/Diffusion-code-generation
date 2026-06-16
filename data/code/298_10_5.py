from datetime import datetime
def calculate_time_difference(time_str1: str, time_str2: str) -> tuple[datetime, datetime]:
    try:
        time1 = datetime.strptime(time_str1, '%H:%M:%S')
        time2 = datetime.strptime(time_str2, '%H:%M:%S')
        return time1, time2
    except ValueError:
        raise ValueError("Invalid time format. Please use 'HH:MM:SS'.")
if __name__ == '__main__':
    time_a = "01:00:00"
    time_b = "05:30:15"
    try:
        start_time, end_time = calculate_time_difference(time_a, time_b)
        difference = end_time - start_time
        print(f"Time 1: {start_time}")
        print(f"Time 2: {end_time}")
        print(f"Difference: {difference}")
    except ValueError as e:
        print(f"Error: {e}")
    time_c = "23:59:59"
    time_d = "00:00:01"
    try:
        start_time, end_time = calculate_time_difference(time_c, time_d)
        difference = end_time - start_time
        print(f"\nTime 1: {start_time}")
        print(f"Time 2: {end_time}")
        print(f"Difference: {difference}")
    except ValueError as e:
        print(f"Error: {e}")
    time_e = "99:99:99"
    time_f = "10:10:10"
    try:
        start_time, end_time = calculate_time_difference(time_e, time_f)
        difference = end_time - start_time
        print(f"\nTime 1: {start_time}")
        print(f"Time 2: {end_time}")
        print(f"Difference: {difference}")
    except ValueError as e:
        print(f"\nError: {e}")