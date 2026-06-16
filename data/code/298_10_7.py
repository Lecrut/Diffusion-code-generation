from datetime import datetime
def calculate_time_difference(time_str1: str, time_str2: str) -> tuple[datetime, datetime] | None:
    time_format = '%H:%M:%S'
    try:
        time1 = datetime.strptime(time_str1, time_format)
        time2 = datetime.strptime(time_str2, time_format)
        return time1, time2
    except ValueError:
        return None
if __name__ == '__main__':
    time_a = "01:00:00"
    time_b = "05:30:15"
    result = calculate_time_difference(time_a, time_b)
    if result:
        time1, time2 = result
        difference = time2 - time1
        print(f"Time 1: {time1}")
        print(f"Time 2: {time2}")
        print(f"Difference: {difference}")
    else:
        print("Error processing time strings.")
    time_c = "23:59:59"
    time_d = "00:00:01"
    result_error = calculate_time_difference(time_c, time_d)
    if result_error is None:
        print("\nError handling test successful (expected failure if times are invalid).")