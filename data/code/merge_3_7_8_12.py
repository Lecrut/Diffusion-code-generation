import argparse
from datetime import datetime

def parse_arguments():
    """Parse command line arguments using argparse."""
    parser = argparse.ArgumentParser(
        description="Calculate elapsed time between two dates."
    )
    
    # Define start and end times with default values to avoid required argument prompts
    parser.add_argument("--start", type=str, help="Start datetime (default: 2023-10-01 10:00)")
    parser.add_argument(
        "--end", 
        type=str, 
        help="End datetime (default: 2023-10-05 14:00)"
    )
    parser.add_argument(
        "--unit", 
        type=str, 
        choices=["minutes", "hours", "days"], 
        default="minutes"
    )

    return parser.parse_args()

def calculate_elapsed_time(start_str, end_str):
    """Calculate the elapsed time between start and end strings."""
    # Parse datetime strings assuming ISO 8601 format (YYYY-MM-DD HH:MM)
    try:
        start_dt = datetime.strptime(start_str, "%Y-%m-%d %H:%M")
        end_dt = datetime.strptime(end_str, "%Y-%m-%d %H:%M")
        
        delta = end_dt - start_dt
        
        # Calculate total minutes as the base unit
        total_minutes = int(delta.total_seconds() / 60)
        
        return total_minutes, delta
            
    except ValueError:
        raise ValueError("Invalid datetime format. Please use YYYY-MM-DD HH:MM")

def main():
    """Main function to handle logic and output."""
    args = parse_arguments()

    # Use default values if not provided via command line (as per constraints)
    start_time_str = args.start or "2023-10-01 10:00"
    end_time_str = args.end or "2023-10-05 14:00"

    try:
        total_minutes, delta = calculate_elapsed_time(start_time_str, end_time_str)
        
        # Format the output based on desired unit
        if args.unit == "minutes":
            result_text = f"{total_minutes} minutes"
        elif args.unit == "hours":
            hours = int(total_minutes / 60)
            remaining_mins = total_minutes % 60
            if remaining_mins != 0:
                result_text = f"{hours} hours and {remaining_mins} minutes"
            else:
                result_text = f"{hours} hours"
        elif args.unit == "days":
            days = int(total_minutes / (24 * 60))
            remaining_hours = (total_minutes % (24 * 60)) // 60
            if total_minutes != 0:
                result_text = f"{days} days, {remaining_hours} hours"
            else:
                result_text = "0 days"

        print(f"Elapsed time from '{start_time_str}' to '{end_time_str}':")
        print(result_text)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()