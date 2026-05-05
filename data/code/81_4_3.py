import datetime
def time_difference_hours(time_str1, time_str2):
    time1 = datetime.datetime.strptime(time_str1, '%H:%M:%S').time()
    time2 = datetime.datetime.strptime(time_str2, '%H:%M:%S').time()
    seconds1 = time1.hour * 3600 + time1.minute * 60 + time1.second
    seconds2 = time2.hour * 3600 + time2.minute * 60 + time2.second
    diff_seconds = abs(seconds1 - seconds2)
    diff_hours = diff_seconds / 3600.0
    return diff_hours
if __name__ == '__main__':
    time1 = '09:00:00'
    time2 = '17:30:00'
    result = time_difference_hours(time1, time2)
    print(result)