import argparse
from datetime import datetime

def calculate_elapsed_time(start_time, end_time, unit='minutes'):
    format_str = "%Y-%m-%d %H:%M:%S"
    start = datetime.strptime(start_time, format_str)
    end = datetime.strptime(end_time, format_str)
    delta = end - start
    
    if unit == 'seconds':
        return delta.total_seconds()
    elif unit == 'minutes':
        return delta.total_seconds() / 60
    elif unit == 'hours':
        return delta.total_seconds() / 3600
    elif unit == 'days':
        return delta.days
    else:
        raise ValueError("Unsupported unit")

if __name__ == '__main__':
    start_time = "2023-10-01 12:00:00"
    end_time = "2023-10-01 13:30:00"
    output_unit = 'minutes'
    
    elapsed_time = calculate_elapsed_time(start_time, end_time, output_unit)
    print(f"Elapsed time in {output_unit}: {elapsed_time}")