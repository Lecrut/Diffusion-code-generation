import datetime

def validate_datetime_format(time_str):
    try:
        datetime.datetime.strptime(time_str, '%H:%M:%S')
        return True
    except ValueError:
        return False

def time_difference_hours(time_str1, time_str2):
    if not (validate_datetime_format(time_str1) and validate_datetime_format(time_str2)):
        raise ValueError("Invalid time format. Please use 'HH:MM:SS'.")

    time1 = datetime.datetime.strptime(time_str1, '%H:%M:%S')
    time2 = datetime.datetime.strptime(time_str2, '%H:%M:%S')

    if time1 > time2:
        time2 += datetime.timedelta(days=1)

    difference = abs((time2 - time1).total_seconds())
    return difference / 3600.0

if __name__ == '__main__':
    time1 = '09:00:00'
    time2 = '17:30:00'
    result = time_difference_hours(time1, time2)
    print(result)