import argparse
from datetime import datetime

def calculate_elapsed_time(start_time, end_time, unit):
    start = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    end = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
    elapsed = end - start
    if unit == 'minutes':
        return elapsed.total_seconds() / 60
    elif unit == 'hours':
        return elapsed.total_seconds() / 3600
    elif unit == 'days':
        return elapsed.days
    else:
        raise ValueError("Unsupported unit. Use 'minutes', 'hours', or 'days'.")
if __name__ == '__main__':
    start_time = '2023-10-01 08:00:00'
    end_time = '2023-10-01 10:30:00'
    unit = 'minutes'
    result = calculate_elapsed_time(start_time, end_time, unit)
    print(result)