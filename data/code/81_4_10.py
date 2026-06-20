import datetime

def time_difference_hours(time_str1, time_str2):
    time_format = '%H:%M:%S'
    time1 = datetime.datetime.strptime(time_str1, time_format)
    time2 = datetime.datetime.strptime(time_str2, time_format)
    delta = abs(time2 - time1)
    difference_seconds = delta.total_seconds()
    difference_hours = difference_seconds / 3600.0
    return difference_hours

if __name__ == '__main__':
    time1 = '09:00:00'
    time2 = '17:30:00'
    result = time_difference_hours(time1, time2)
    print(result)