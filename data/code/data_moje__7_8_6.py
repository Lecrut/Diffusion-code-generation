import argparse
from datetime import datetime

def calculate_elapsed_time(start_time_str, end_time_str, unit='minutes'):
    start_dt = datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')
    end_dt = datetime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S')
    delta = end_dt - start_dt
    total_seconds = delta.total_seconds()
    if unit == 'minutes':
        return total_seconds / 60
    elif unit == 'hours':
        return total_seconds / 3600
    elif unit == 'seconds':
        return total_seconds
    else:
        raise ValueError(f"Unsupported unit: {unit}")

def main():
    parser = argparse.ArgumentParser(description='Calculate elapsed time between two timestamps.')
    parser.add_argument('--start', type=str, default='2023-01-01 00:00:00')
    parser.add_argument('--end', type=str, default='2023-01-01 02:30:45')
    parser.add_argument('--unit', type=str, default='minutes', choices=['minutes', 'hours', 'seconds'])
    args = parser.parse_args()
    result = calculate_elapsed_time(args.start, args.end, args.unit)
    print(result)

if __name__ == '__main__':
    main()