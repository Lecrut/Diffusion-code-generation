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
    parser = argparse.ArgumentParser(description='Calculate elapsed time between two timestamps.')
    parser.add_argument('start_time', type=str, help='Start time in YYYY-MM-DD HH:MM:SS format')
    parser.add_argument('end_time', type=str, help='End time in YYYY-MM-DD HH:MM:SS format')
    parser.add_argument('unit', type=str, choices=['minutes', 'hours', 'days'], help='Desired output unit')

    args = parser.parse_args()

    result = calculate_elapsed_time(args.start_time, args.end_time, args.unit)
    print(result)