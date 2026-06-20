import argparse
import datetime

def calculate_elapsed_time(start_time_str, end_time_str, output_unit):
    fmt = "%Y-%m-%d %H:%M:%S"
    start_dt = datetime.datetime.strptime(start_time_str, fmt)
    end_dt = datetime.datetime.strptime(end_time_str, fmt)
    delta = end_dt - start_dt
    total_seconds = int(delta.total_seconds())
    if output_unit == "seconds":
        return total_seconds
    elif output_unit == "minutes":
        return total_seconds / 60.0
    elif output_unit == "hours":
        return total_seconds / 3600.0
    elif output_unit == "days":
        return total_seconds / 86400.0
    else:
        raise ValueError(f"Unsupported output unit: {output_unit}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Calculate elapsed time between two timestamps.")
    parser.add_argument("--start", type=str, default="2023-01-01 00:00:00", help="Start time in 'YYYY-MM-DD HH:MM:SS' format")
    parser.add_argument("--end", type=str, default="2023-01-01 01:30:00", help="End time in 'YYYY-MM-DD HH:MM:SS' format")
    parser.add_argument("--unit", type=str, default="minutes", choices=["seconds", "minutes", "hours", "days"], help="Output unit")
    args = parser.parse_args()
    result = calculate_elapsed_time(args.start, args.end, args.unit)
    print(result)