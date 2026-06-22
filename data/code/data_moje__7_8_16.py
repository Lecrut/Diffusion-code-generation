import argparse
from datetime import datetime
import sys

def parse_time(time_str):
    return datetime.strptime(time_str, "%H:%M")

def calculate_elapsed_minutes(start_time, end_time):
    delta = end_time - start_time
    total_seconds = int(delta.total_seconds())
    if total_seconds < 0:
        total_seconds += 86400
    return total_seconds // 60

def main():
    parser = argparse.ArgumentParser(description="Calculate elapsed time")
    parser.add_argument('--start', type=str, default='09:00')
    parser.add_argument('--end', type=str, default='10:30')
    parser.add_argument('--unit', type=str, default='minutes')
    args = parser.parse_args([])

    start_dt = parse_time(args.start)
    end_dt = parse_time(args.end)
    elapsed = calculate_elapsed_minutes(start_dt, end_dt)
    print(elapsed)

if __name__ == '__main__':
    main()