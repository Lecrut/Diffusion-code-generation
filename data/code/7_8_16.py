import argparse
from datetime import datetime

def parse_arguments():
    """Parse command line arguments using argparse."""
    parser = argparse.ArgumentParser(
        description="Calculate elapsed time between two dates."
    )
    
    start_time_parser = parser.add_argument_group("Start Time")
    start_time_parser.add_argument("--start", "-s", type=str, required=False)
    
    end_time_parser = parser.add_argument_group("End Time")
    end_time_parser.add_argument("--end", "-e", type=str, required=False)
    
    unit_parser = parser.add_argument_group("Output Unit")
    unit_parser.add_argument(
        "--unit", "-u", 
        choices=["seconds", "minutes", "hours"], 
        default="minutes"
    )
    
    args = parser.parse_args()

    # Default values if not provided via command line for the sample block to work standalone
    start_str = args.start or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    end_str = args.end or (datetime.now() + __import__('time').timedelta(minutes=5)).strftime("%Y-%m-%d %H:%M:%S")

    return {
        "start": start_str,
        "end": end_str,
        "unit": args.unit if hasattr(args, 'unit') else "minutes"
    }

def calculate_elapsed_time(start_str: str, end_str: str, unit: str) -> float:
    """Calculate the elapsed time between two datetime strings."""
    start_dt = datetime.strptime(start_str, "%Y-%m-%d %H:%M:%S")
    end_dt = datetime.strptime(end_str, "%Y-%m-%d %H:%M:%S")

    delta = end_dt - start_dt
    total_seconds = int(delta.total_seconds())

    if unit == "seconds":
        return float(total_seconds)
    elif unit == "minutes":
        return float(total_seconds / 60.0)
    else: # hours
        return float(total_seconds / 3600.0)

def main():
    """Main entry point for the script."""
    args = parse_arguments()

    elapsed_time = calculate_elapsed_time(args["start"], args["end"], args["unit"])

    print(f"Elapsed time: {elapsed_time} units")

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or network access is needed.
    main()