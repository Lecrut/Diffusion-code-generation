import datetime

def calculate_timezone_difference(timezone1, timezone2):
    tz1 = datetime.timezone(datetime.timedelta(hours=timezone1))
    tz2 = datetime.timezone(datetime.timedelta(hours=timezone2))
    difference = (tz2.utcoffset(None) - tz1.utcoffset(None)).total_seconds() / 3600
    return difference
if __name__ == '__main__':
    timezone1 = 5
    timezone2 = -3
    difference_hours = calculate_timezone_difference(timezone1, timezone2)
    print(difference_hours)