import argparse
from datetime import datetime

def calculate_elapsed_time(start_time, end_time, unit):
    start = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
    end = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
    delta = (end - start).total_seconds()
    if unit == 'minutes':
        return delta / 60
    elif unit == 'hours':
        return delta / 3600
    else:
        raise ValueError("Unsupported unit. Please choose 'minutes' or 'hours'.")
if __name__ == '__main__':
    start_time = '2023-10-01 12:00:00'
    end_time = '2023-10-01 13:30:00'
    unit = 'minutes'
    try:
        elapsed_time = calculate_elapsed_time(start_time, end_time, unit)
        print(f'Elapsed time: {elapsed_time} {unit}')
    except ValueError as e:
        print(e)