import sys
from datetime import datetime
if __name__ == '__main__':
    timestamp1_str = "2023-01-01 10:00:00"
    timestamp2_str = "2023-01-05 14:30:00"
    time1 = datetime.strptime(timestamp1_str, "%Y-%m-%d %H:%M:%S")
    time2 = datetime.strptime(timestamp2_str, "%Y-%m-%d %H:%M:%S")
    time_difference = time2 - time1
    days = time_difference.days
    hours = time_difference.seconds // 3600
    minutes = (time_difference.seconds % 3600) // 60
    seconds = time_difference.seconds % 60
    print(f"Time elapsed: {days} days, {hours} hours, {minutes} minutes")