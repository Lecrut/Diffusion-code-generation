import argparse
from datetime import datetime

def calculate_elapsed_time(start_time, end_time, unit):
    start = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    end = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
    elapsed_seconds = (end - start).total_seconds()
    if unit == 'minutes':
        return elapsed_seconds / 60
    elif unit == 'hours':
        return elapsed_seconds / 3600
    elif unit == 'days':
        return elapsed_seconds / 86400
    else:
        raise ValueError("Unsupported unit. Use 'minutes', 'hours', or 'days'.")
if __name__ == '__main__':
    start_time = '2023-10-01 12:00:00'
    end_time = '2023-10-01 14:30:00'
    unit = 'minutes'
    try:
        result = calculate_elapsed_time(start_time, end_time, unit)
        print(result)
    except ValueError as e:
        print(e)