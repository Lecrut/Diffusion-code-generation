import argparse
from datetime import datetime

def calculate_elapsed_time(start_str, end_str, unit):
    start = datetime.strptime(start_str, "%Y-%m-%d %H:%M:%S")
    end = datetime.strptime(end_str, "%Y-%m-%d %H:%M:%S")
    delta = end - start
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

def parse_args():
    parser = argparse.ArgumentParser(description="Calculate elapsed time between two timestamps.")
    parser.add_argument("start_time", help="Start time in YYYY-MM-DD HH:MM:SS format")
    parser.add_argument("end_time", help="End time in YYYY-MM-DD HH:MM:SS format")
    parser.add_argument("unit", choices=["seconds", "minutes", "hours", "days"], help="Output unit")
    return parser.parse_args()

if __name__ == "__main__":
    import sys
    sys.argv = ["script_name", "2023-01-01 10:00:00", "2023-01-01 12:30:00", "minutes"]
    args = parse_args()
    result = calculate_elapsed_time(args.start_time, args.end_time, args.unit)
    print(result)