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
    time_b = "03:30:45"
    result = calculate_time_difference(time_a, time_b)
    if result:
        t1, t2 = result
        difference = t2 - t1
        print(f"Time 1: {t1}")
        print(f"Time 2: {t2}")
        print(f"Difference: {difference}")
    else:
        print("Error processing time strings.")
    time_c = "25:00:00"
    time_d = "10:00:00"
    result_error = calculate_time_difference(time_c, time_d)
    if result_error is None:
        print("\nError handling successful for invalid time format.")