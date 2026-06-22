import argparse
from datetime import datetime

def calculate_elapsed_time(start_str, end_str, unit):
    fmt = "%Y-%m-%d %H:%M:%S"
    start_dt = datetime.strptime(start_str, fmt)
    end_dt = datetime.strptime(end_str, fmt)
    delta = end_dt - start_dt
    total_seconds = delta.total_seconds()
    if unit == "seconds":
        return total_seconds
    elif unit == "minutes":
        return total_seconds / 60
    elif unit == "hours":
        return total_seconds / 3600
    elif unit == "days":
        return total_seconds / 86400
    else:
        raise ValueError(f"Unsupported unit: {unit}")

def create_parser():
    parser = argparse.ArgumentParser(description="Calculate elapsed time")
    parser.add_argument("--start", required=True, help="Start time (YYYY-MM-DD HH:MM:SS)")
    parser.add_argument("--end", required=True, help="End time (YYYY-MM-DD HH:MM:SS)")
    parser.add_argument("--unit", choices=["seconds", "minutes", "hours", "days"], default="minutes", help="Output unit")
    return parser

if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args([])
    args.start = "2023-01-01 10:00:00"
    args.end = "2023-01-01 12:30:00"
    args.unit = "minutes"
    result = calculate_elapsed_time(args.start, args.end, args.unit)
    print(result)