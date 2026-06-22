import argparse
from datetime import datetime

def calculate_elapsed_time(start_time_str, end_time_str, output_unit):
    start_dt = datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S")
    end_dt = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M:%S")
    delta = end_dt - start_dt
    total_seconds = delta.total_seconds()
    if output_unit == 'minutes':
        return total_seconds / 60
    elif output_unit == 'hours':
        return total_seconds / 3600
    elif output_unit == 'seconds':
        return total_seconds
    elif output_unit == 'days':
        return total_seconds / 86400
    else:
        raise ValueError(f"Unsupported unit: {output_unit}")

def create_parser():
    parser = argparse.ArgumentParser(description='Calculate elapsed time between two datetime strings.')
    parser.add_argument('--start', type=str, help='Start time in format YYYY-MM-DD HH:MM:SS')
    parser.add_argument('--end', type=str, help='End time in format YYYY-MM-DD HH:MM:SS')
    parser.add_argument('--unit', type=str, choices=['minutes', 'hours', 'seconds', 'days'],
                        help='Desired output unit for the elapsed time')
    return parser

if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args(['--start', '2023-10-01 12:00:00', '--end', '2023-10-01 14:30:00', '--unit', 'minutes'])
    result = calculate_elapsed_time(args.start, args.end, args.unit)
    print(result)