import argparse
from datetime import datetime

def calculate_elapsed_time(start_time_str, end_time_str, unit):
    start_time = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')
    end_time = datetime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S')
    elapsed_time = end_time - start_time
    
    if unit == 'minutes':
        return elapsed_time.total_seconds() / 60
    elif unit == 'hours':
        return elapsed_time.total_seconds() / 3600
    elif unit == 'days':
        return elapsed_time.days
    else:
        raise ValueError("Unsupported unit. Use 'minutes', 'hours', or 'days'.")

if __name__ == '__main__':
    start_time = '2023-10-01 09:00:00'
    end_time = '2023-10-01 12:30:00'
    unit = 'minutes'
    
    elapsed = calculate_elapsed_time(start_time, end_time, unit)
    print(elapsed)