import datetime
def calculate_time_difference(dt1, dt2):
    if dt1 > dt2:
        diff = dt1 - dt2
    else:
        diff = dt2 - dt1
    total_seconds = int(diff.total_seconds())
    days = total_seconds // 86400
    remaining_seconds = total_seconds % 86400
    hours = remaining_seconds // 3600
    remaining_seconds %= 3600
    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60
    return {
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds
    }
if __name__ == '__main__':
    time1 = datetime.datetime(2023, 1, 1, 10, 30, 45)
    time2 = datetime.datetime(2023, 1, 5, 15, 50, 10)
    difference = calculate_time_difference(time1, time2)
    print(f"Time difference between {time1} and {time2}:")
    print(f"Days: {difference['days']}")
    print(f"Hours: {difference['hours']}")
    print(f"Minutes: {difference['minutes']}")
    print(f"Seconds: {difference['seconds']}")