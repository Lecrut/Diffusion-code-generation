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
    time1 = datetime.datetime(2023, 10, 26, 14, 30, 15)
    time2 = datetime.datetime(2023, 10, 28, 9, 15, 40)
    result = calculate_time_difference(time1, time2)
    print(result)