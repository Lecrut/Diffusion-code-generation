from datetime import datetime

def time_difference_in_seconds(time_str1, time_str2):
    time_format = '%H:%M:%S'
    time1 = datetime.strptime(time_str1, time_format)
    time2 = datetime.strptime(time_str2, time_format)
    delta = time2 - time1
    return abs(delta.total_seconds())
if __name__ == '__main__':
    time_point1 = '14:30:00'
    time_point2 = '15:45:00'
    difference = time_difference_in_seconds(time_point1, time_point2)
    print(difference)