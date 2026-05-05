import datetime
def time_difference(date1_str, date2_str):
    date1 = datetime.datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
    date2 = datetime.datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")
    if date1 > date2:
        diff = date1 - date2
    else:
        diff = date2 - date1
    total_seconds = int(diff.total_seconds())
    hours = total_seconds // 3600
    remaining_seconds = total_seconds % 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return hours, minutes, seconds
if __name__ == '__main__':
    date_a = "2023-01-01 10:00:00"
    date_b = "2023-01-03 14:30:15"
    h, m, s = time_difference(date_a, date_b)
    print(f"Date 1: {date_a}")
    print(f"Date 2: {date_b}")
    print(f"Difference in hours: {h}")
    print(f"Difference in minutes: {m}")
    print(f"Difference in seconds: {s}")