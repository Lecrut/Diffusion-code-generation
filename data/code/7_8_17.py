import argparse
from datetime import datetime
from typing import Tuple

def parse_time(time_str: str) -> datetime:
    return datetime.strptime(time_str, "%H:%M:%S")

def calculate_elapsed_time(start_time_str: str, end_time_str: str, output_unit: str) -> float:
    start_time = parse_time(start_time_str)
    end_time = parse_time(end_time_str)
    
    if end_time < start_time:
        end_time += datetime(1900, 1, 1) - datetime(1900, 1, 1) + timedelta(days=1)
    
    delta = end_time - start_time
    total_seconds = delta.total_seconds()
    
    if output_unit == "minutes":
        return total_seconds / 60
    elif output_unit == "hours":
        return total_seconds / 3600
    elif output_unit == "seconds":
        return total_seconds
    else:
        raise ValueError(f"Unsupported unit: {output_unit}. Use 'minutes', 'hours', or 'seconds'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate elapsed time between two times.")
    parser.add_argument("--start", type=str, required=True, help="Start time in HH:MM:SS format")
    parser.add_argument("--end", type=str, required=True, help="End time in HH:MM:SS format")
    parser.add_argument("--unit", type=str, required=True, choices=["minutes", "hours", "seconds"], help="Output unit")
    
    args = parser.parse_args()
    
    result = calculate_elapsed_time(args.start, args.end, args.unit)
    print(f"Elapsed time: {result} {args.unit}")