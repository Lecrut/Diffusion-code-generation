import argparse
from datetime import datetime

def parse_time(time_str, fmt="%H:%M:%S"):
    return datetime.strptime(time_str, fmt)

def calculate_elapsed_seconds(start, end):
    delta = end - start
    total_seconds = delta.total_seconds()
    if total_seconds < 0:
        total_seconds += 86400
    return total_seconds

def convert_elapsed_time(total_seconds, unit):
    if unit == 'minutes':
        return total_seconds / 60.0
    elif unit == 'hours':
        return total_seconds / 3600.0
    elif unit == 'seconds':
        return total_seconds
    else:
        raise ValueError(f"Unsupported unit: {unit}")

def calculate_total_elapsed_time(start_str, end_str, unit):
    start_time = parse_time(start_str)
    end_time = parse_time(end_str)
    total_seconds = calculate_elapsed_seconds(start_time, end_time)
    result = convert_elapsed_time(total_seconds, unit)
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate elapsed time between two timestamps.')
    parser.add_argument('--start', type=str, default='09:00:00', help='Start time in HH:MM:SS format')
    parser.add_argument('--end', type=str, default='10:30:45', help='End time in HH:MM:SS format')
    parser.add_argument('--unit', type=str, default='minutes', choices=['seconds', 'minutes', 'hours'], help='Output unit')
    args = parser.parse_args([])

    result = calculate_total_elapsed_time(args.start, args.end, args.unit)
    print(result)