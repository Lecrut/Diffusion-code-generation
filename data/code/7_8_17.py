import argparse
from datetime import datetime

def parse_time(time_str: str) -> datetime:
    """Parse a time string in 'HH:MM' format into a datetime object."""
    try:
        return datetime.strptime(time_str, "%H:%M")
    except ValueError as e:
        raise SystemExit(f"Error parsing time '{time_str}': {e}")

def calculate_elapsed_time(start_dt: datetime, end_dt: datetime) -> int:
    """Calculate the elapsed time in minutes between two datetime objects."""
    delta = end_dt - start_dt
    return int(delta.total_seconds() / 60)

def main():
    parser = argparse.ArgumentParser(
        description="Calculate the total elapsed time between a start and an end time."
    )

    # Define non-interactive arguments with defaults to ensure no user input is required.
    parser.add_argument("--start", type=str, default="10:30", help="Start time in HH:MM format.")
    parser.add_argument("--end", type=str, default="14:45", help="End time in HH:MM format.")
    parser.add_argument(
        "--unit",
        type=str,
        choices=["minutes"],
        default="minutes",
        help="Desired output unit (currently only 'minutes' is supported).",
    )

    args = parser.parse_args()

    try:
        start_time = parse_time(args.start)
        end_time = parse_time(args.end)
        
        elapsed_minutes = calculate_elapsed_time(start_time, end_time)
        
        print(f"Elapsed time from {args.start} to {args.end}: {elapsed_minutes} {args.unit}")

    except SystemExit as e:
        # Re-raise if it's an error exit (e.g., invalid arguments), otherwise ignore.
        raise

if __name__ == "__main__":
    main()