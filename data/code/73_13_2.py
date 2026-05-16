import sys
from datetime import datetime
def calculate_time_difference(date_str1, date_str2):
    try:
        dt1 = datetime.strptime(date_str1, '%Y-%m-%d %H:%M:%S')
        dt2 = datetime.strptime(date_str2, '%Y-%m-%d %H:%M:%S')
        time_difference = abs(dt1 - dt2)
        return int(time_difference.total_seconds())
    except ValueError:
        return -1
if __name__ == '__main__':
    date1_str = "2023-10-27 10:00:00"
    date2_str = "2023-10-27 10:05:30"
    result = calculate_time_difference(date1_str, date2_str)
    print(result)