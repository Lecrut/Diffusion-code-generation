import datetime

def parse_time_str(time_str):
    try:
        return datetime.datetime.strptime(time_str, '%H:%M:%S').time()
    except ValueError as e:
        raise ValueError("Invalid time format. Please use HH:MM:SS.") from e

def time_difference_hours(time_str1, time_str2):
    time1 = parse_time_str(time_str1)
    time2 = parse_time_str(time_str2)
    t1 = time1.hour * 3600 + time1.minute * 60 + time1.second
    t2 = time2.hour * 3600 + time2.minute * 60 + time2.second
    difference_seconds = abs(t1 - t2)
    difference_hours = difference_seconds / 3600.0
    return difference_hours

if __name__ == '__main__':
    time1 = '09:00:00'
    time2 = '17:30:00'
    result = time_difference_hours(time1, time2)
    print(result)