import argparse
from datetime import datetime

def parse_arguments():
    """Parse command line arguments using argparse."""
    parser = argparse.ArgumentParser(
        description="Calculate elapsed time between two timestamps."
    )
    
    start_time_parser = parser.add_argument_group("Start Time")
    start_time_parser.add_argument("--start", type=str, required=False, help="Start timestamp (YYYY-MM-DD HH:MM:SS)")
    
    end_time_parser = parser.add_argument_group("End Time")
    end_time_parser.add_argument("--end", type=str, required=False, help="End timestamp (YYYY-MM-DD HH:MM:SS)")
    
    unit_parser = parser.add_argument_group("Output Unit")
    unit_parser.add_argument(
        "--unit", 
        type=str, 
        default='minutes', 
        choices=['seconds', 'minutes', 'hours'], 
        help="Desired output unit for elapsed time (default: minutes)"
    )
    
    args = parser.parse_args()
    
    # Set defaults if not provided to ensure the script runs without input prompts or required arguments failing silently in a non-interactive way.
    # Using fixed sample values as per task requirements when no CLI args are passed via stdin (which is forbidden).
    default_start_str = "2023-10-01 10:00:00"
    default_end_str = "2023-10-01 14:30:00"
    
    if not args.start or not args.end:
        # Since input() and sys.stdin are forbidden, we use the defaults directly here.
        start_time_str = default_start_str
        end_time_str = default_end_str
    
    return {
        'start': datetime.strptime(start_time_str, "%Y-%m-%d %H:%M:%S"),
        'end': datetime.strptime(end_time_str, "%Y-%m-%d %H:%M:%S"),
        'unit': args.unit or 'minutes'
    }

def calculate_elapsed_time(start: datetime, end: datetime, unit: str) -> float:
    """Calculate the elapsed time between start and end in the specified unit."""
    delta = end - start
    
    if unit == "seconds":
        return delta.total_seconds()
    elif unit == "minutes":
        return delta.total_seconds() / 60.0
    else: # hours
        return delta.total_seconds() / 3600.0

def main():
    """Main function to execute the logic."""
    try:
        config = parse_arguments()
        
        elapsed_time = calculate_elapsed_time(
            start=config['start'], 
            end=config['end'], 
            unit=config['unit']
        )
        
        print(f"Elapsed time from {config['start'].strftime('%Y-%m-%d %H:%M:%S')} to "
              f"{config['end'].strftime('%Y-%m-%d %H:%M:%S')}:")
        print(f"Total: {elapsed_time:.2f} {config['unit']}")
        
    except ValueError as e:
        # Handle cases where the date format is incorrect, though sample values are correct.
        print(f"Error parsing dates: {e}")

if __name__ == '__main__':
    main()