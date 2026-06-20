import argparse
import sys

def parse_time(time_str):
    parts = time_str.split(':')
    if len(parts) != 3:
        raise ValueError("Time must be in HH:MM:SS format")
    return int(parts[0]) * 3600 + int(parts[1]) * 60 + int(parts[2])

def calculate_elapsed_time(start_seconds, end_seconds):
    return end_seconds - start_seconds

def convert_time(total_seconds, unit):
    if unit == 'seconds':
        return total_seconds
    if unit == 'minutes':
        return total_seconds / 60.0
    if unit == 'hours':
        return total_seconds / 3600.0
    raise ValueError(f"Unsupported unit: {unit}")

def run(cli_args):
    parser = argparse.ArgumentParser(description='Calculate elapsed time')
    parser.add_argument('start_time', help='Start time in HH:MM:SS')
    parser.add_argument('end_time', help='End time in HH:MM:SS')
    parser.add_argument('unit', choices=['seconds', 'minutes', 'hours'], default='seconds', help='Output unit')
    
    args = parser.parse_args(cli_args)
    
    try:
        start_seconds = parse_time(args.start_time)
        end_seconds = parse_time(args.end_time)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
        
    if end_seconds < start_seconds:
        print("Error: End time must be after start time")
        sys.exit(1)
        
    elapsed = calculate_elapsed_time(start_seconds, end_seconds)
    result = convert_time(elapsed, args.unit)
    return result

if __name__ == '__main__':
    result = run(['01:30:00', '02:15:30', 'minutes'])
    print(result)