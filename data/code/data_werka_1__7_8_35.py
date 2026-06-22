import argparse
from datetime import datetime

def calculate_elapsed_time(start_time_str, end_time_str, output_unit):
    start_time = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')
    end_time = datetime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S')
    elapsed_time = end_time - start_time
    
    if output_unit == 'seconds':
        return elapsed_time.total_seconds()
    elif output_unit == 'minutes':
        return elapsed_time.total_seconds() / 60
    elif output_unit == 'hours':
        return elapsed_time.total_seconds() / 3600
    else:
        raise ValueError("Unsupported unit. Use 'seconds', 'minutes', or 'hours'.")

if __name__ == '__main__':
    start_time = "2023-10-01 12:00:00"
    end_time = "2023-10-01 14:30:00"
    output_unit = 'minutes'
    
    elapsed = calculate_elapsed_time(start_time, end_time, output_unit)
    print(elapsed)