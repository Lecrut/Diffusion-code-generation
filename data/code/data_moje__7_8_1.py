import argparse
from datetime import datetime
import time

def parse_time(time_string):
    return datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S")

def calculate_elapsed(start_time_str, end_time_str, unit):
    start_dt = parse_time(start_time_str)
    end_dt = parse_time(end_time_str)
    delta = end_dt - start_dt
    total_seconds = delta.total_seconds()
    if unit == "minutes":
        return total_seconds / 60
    elif unit == "hours":
        return total_seconds / 3600
    elif unit == "days":
        return total_seconds / 86400
    elif unit == "seconds":
        return total_seconds
    else:
        raise ValueError("Unsupported unit")

def main():
    parser = argparse.ArgumentParser(description="Calculate elapsed time between two timestamps.")
    parser.add_argument("start_time", type=str, help="Start time in YYYY-MM-DD HH:MM:SS format")
    parser.add_argument("end_time", type=str, help="End time in YYYY-MM-DD HH:MM:SS format")
    parser.add_argument("unit", type=str, help="Output unit: minutes, hours, days, or seconds")
    args = parser.parse_args()
    result = calculate_elapsed(args.start_time, args.end_time, args.unit)
    print(result)

if __name__ == '__main__':
    sample_start = "2023-10-01 10:00:00"
    sample_end = "2023-10-01 12:30:00"
    sample_unit = "minutes"
    result = calculate_elapsed(sample_start, sample_end, sample_unit)
    print(result)