from datetime import datetime
def calculate_time_difference(time_str1: str, time_str2: str) -> tuple[datetime, datetime] | None:
    try:
        format_str = '%H:%M:%S'
        dt1 = datetime.strptime(time_str1, format_str)
        dt2 = datetime.strptime(time_str2, format_str)
        return dt1, dt2
    except ValueError:
        return None
if __name__ == '__main__':
    time1 = "01:00:00"
    time2 = "03:45:30"
    result = calculate_time_difference(time1, time2)
    if result:
        dt1, dt2 = result
        difference = abs(dt2 - dt1)
        print(f"Time 1: {dt1}")
        print(f"Time 2: {dt2}")
        print(f"Time Difference: {difference}")
    else:
        print("Error processing time strings.")