import argparse
import sys
from datetime import datetime

def calculate_elapsed_time(start_str, end_str, unit):
    fmt = "%H:%M:%S"
    start_dt = datetime.strptime(start_str, fmt)
    end_dt = datetime.strptime(end_str, fmt)
    delta = end_dt - start_dt
    total_seconds = int(delta.total_seconds())
    if total_seconds < 0:
        total_seconds += 86400
    if unit == 'seconds':
        return total_seconds
    if unit == 'minutes':
        return total_seconds / 60.0
    if unit == 'hours':
        return total_seconds / 3600.0
    raise ValueError(f"Unsupported unit: {unit}")

def build_parser():
    parser = argparse.ArgumentParser(description="Calculate elapsed time between two timestamps.")
    parser.add_argument("--start", type=str, help="Start time in HH:MM:SS format")
    parser.add_argument("--end", type=str, help="End time in HH:MM:SS format")
    parser.add_argument("--unit", type=str, default='seconds', help="Output unit: seconds, minutes, or hours")
    return parser

if __name__ == '__main__':
    parser = build_parser()
    args = parser.parse_args()
    
    if not args.start:
        args.start = "10:00:00"
    if not args.end:
        args.end = "12:30:45"
    if not args.unit:
        args.unit = 'minutes'
    
    result = calculate_elapsed_time(args.start, args.end, args.unit)
    print(result)