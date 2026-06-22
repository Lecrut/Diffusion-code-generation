from datetime import datetime, timedelta
HOUR_TO_SECONDS = 3600

def calculate_time_difference():
    time1 = datetime.strptime('23:59', '%H:%M')
    time2 = datetime.strptime('00:01', '%H:%M') + timedelta(days=1)
    if time2 < time1:
        time2 += timedelta(days=1)
    difference = (time2 - time1).total_seconds()
    return difference
if __name__ == '__main__':
    diff_seconds = calculate_time_difference()
    print(diff_seconds)