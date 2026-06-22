import argparse
from datetime import datetime

def calculate_elapsed_time(start_time, end_time, unit):
    format_str = '%Y-%m-%d %H:%M:%S'
    start = datetime.strptime(start_time, format_str)
    end = datetime.strptime(end_time, format_str)
    elapsed = end - start
    
    if unit == 'minutes':
        return elapsed.total_seconds() / 60
    elif unit == 'hours':
        return elapsed.total_seconds() / 3600
    elif unit == 'days':
        return elapsed.days
    else:
        raise ValueError("Unsupported unit")

if __name__ == '__main__':
    start_time = "2023-10-01 12:00:00"
    end_time = "2023-10-01 14:30:00"
    unit = 'minutes'
    
    try:
        result = calculate_elapsed_time(start_time, end_time, unit)
        print(result)
    except ValueError as e:
        print(e)