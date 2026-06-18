import argparse

def convert_time(hours: float, minutes: int) -> None:
    """Converts hours to total minutes."""
    return hours * 60 + minutes

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert time between hours and minutes.")
    
    # Define non-required arguments with defaults for the sample run
    hour_arg = parser.add_argument(
        '--hours', 
        type=float, 
        default=2.5,  # Hard-coded sample value: 2.5 hours
        help='Number of hours (default: 2.5)'
    )
    
    minute_arg = parser.add_argument(
        '--minutes', 
        type=int, 
        default=30,   # Hard-coded sample value: 30 minutes
        help='Additional minutes in seconds or as part of the time (default: 30)'
    )

    args = parser.parse_args()
    
    total_minutes = convert_time(args.hours, args.minutes)
    print(f"{args.hours} hours and {args.minutes} minutes is equal to {total_minutes:.2f} minutes.")