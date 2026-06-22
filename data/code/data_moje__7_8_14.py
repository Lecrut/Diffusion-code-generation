import argparse
import datetime
import sys

def calculate_elapsed_time(start_time: str, end_time: str, output_unit: str) -> float:
    fmt = "%H:%M:%S"
    start_dt = datetime.datetime.strptime(start_time, fmt)
    end_dt = datetime.datetime.strptime(end_time, fmt)
    delta = end_dt - start_dt
    total_seconds = delta.total_seconds()
    if output_unit == "seconds":
        return total_seconds
    elif output_unit == "minutes":
        return total_seconds / 60.0
    elif output_unit == "hours":
        return total_seconds / 3600.0
    else:
        raise ValueError(f"Unsupported output unit: {output_unit}")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Calculate elapsed time.")
    parser.add_argument("--start", type=str, required=True, help="Start time in HH:MM:SS")
    parser.add_argument("--end", type=str, required=True, help="End time in HH:MM:SS")
    parser.add_argument("--unit", type=str, default="seconds", choices=["seconds", "minutes", "hours"], help="Output unit")
    return parser.parse_args()

if __name__ == '__main__':
    args = argparse.Namespace(start="09:00:00", end="10:30:00", unit="minutes")
    result = calculate_elapsed_time(args.start, args.end, args.unit)
    print(result)