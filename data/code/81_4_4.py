import datetime
def time_difference_hours(time_str1, time_str2):
    time1 = datetime.datetime.strptime(time_str1, '%H:%M:%S')
    time2 = datetime.datetime.strptime(time_str2, '%H:%M:%S')
    diff = abs(time1 - time2)
    return diff.total_seconds() / 3600
if __name__ == '__main__':
    time1 = '09:00:00'
    time2 = '17:30:00'
    result = time_difference_hours(time1, time2)
    print(result)