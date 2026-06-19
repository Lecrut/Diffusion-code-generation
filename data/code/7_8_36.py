import argparse
from datetime import datetime

def calculate_elapsed_time(start_time, end_time, unit):
    start = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    end = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
    delta = end - start
    total_seconds = delta.total_seconds()
    if unit == 'minutes':
        return total_seconds / 60
    elif unit == 'hours':
        return total_seconds / 3600
    elif unit == 'days':
        return total_seconds / (3600 * 24)
    else:
        return total_seconds
if __name__ == '__main__':
    start_time = '2023-10-01 12:00:00'
    end_time = '2023-10-01 14:30:00'
    unit = 'minutes'
    result = calculate_elapsed_time(start_time, end_time, unit)
    print(f'Elapsed time in {unit}: {result}')