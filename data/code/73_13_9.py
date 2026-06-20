import sys
from datetime import datetime

SECONDS_PER_MINUTE = 60
MINUTES_PER_HOUR = 60
HOURS_PER_DAY = 24

def calculate_time_difference(date_str1, date_str2):
    try:
        dt1 = datetime.strptime(date_str1, '%Y-%m-%dT%H:%M:%S')
        dt2 = datetime.strptime(date_str2, '%Y-%m-%dT%H:%M:%S')
        time_difference = abs(dt1 - dt2)
        
        total_seconds = (time_difference.days * HOURS_PER_DAY * MINUTES_PER_HOUR * SECONDS_PER_MINUTE) + \
                       (time_difference.seconds // SECONDS_PER_MINUTE)
        
        return int(total_seconds)
    except ValueError:
        return -1

if __name__ == '__main__':
    date1_input = "2023-10-27T10:00:00"
    date2_input = "2023-10-27T10:05:30"
    result = calculate_time_difference(date1_input, date2_input)
    print(result)