import sys
from datetime import datetime
ISO_FORMAT = '%Y-%m-%d %H:%M:%S'

def calculate_time_difference(date_str1, date_str2):
    try:
        date1 = datetime.strptime(date_str1, ISO_FORMAT)
        date2 = datetime.strptime(date_str2, ISO_FORMAT)
        time_difference = abs(date1 - date2)
        return int(time_difference.total_seconds())
    except ValueError:
        return -1
if __name__ == '__main__':
    sample_date1 = '2023-10-27 10:00:00'
    sample_date2 = '2023-10-27 10:05:30'
    result = calculate_time_difference(sample_date1, sample_date2)
    print(result)