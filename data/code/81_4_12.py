from datetime import datetime

def time_difference_hours(time_str1, time_str2):
    time_format = '%H:%M:%S'
    time1 = datetime.strptime(time_str1, time_format)
    time2 = datetime.strptime(time_str2, time_format)
    difference = abs((time2 - time1).total_seconds())
    return difference / 3600

if __name__ == '__main__':
    time1 = '09:00:00'
    time2 = '17:30:00'
    result = time_difference_hours(time1, time2)
    print(result)