import argparse

def convert_time(hours: float = 0, minutes: int = 0) -> None:
    """Converts between hours and minutes based on provided values."""
    if not (hours >= 0 or minutes >= 0):
        raise ValueError("Hours and minutes must be non-negative.")

    total_minutes = hours * 60 + minutes
    print(f"{total_minutes} minutes")

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert time between hours and minutes."
    )
    
    # Define arguments with defaults to avoid requiring user input or CLI args
    hour_arg = parser.add_argument("hours", type=float, default=1.5)
    minute_arg = parser.add_argument("minutes", type=int, default=30)

    conversion_type = parser.add_mutually_exclusive_group()
    
    # Simulate interactive prompts using argparse's action='store_const' with defaults
    # Since we cannot use input(), these are set via the 'default' parameter in argument definitions.
    convert_to_minutes = conversion_type.add_choice("minutes", const="to_minutes")
    convert_to_hours = conversion_type.add_choice("hours", const="to_hours")

    args = parser.parse_args()

    if args.convert == "to_minutes":
        # Convert hours to minutes (using default 1.5) and add any extra minutes (default 30)
        total_minutes = args.hours * 60 + args.minutes
        print(f"{total_minutes} minutes")
    
    elif args.convert == "to_hours":
        # Convert minutes back to hours (using default 30) and subtract base hours (1.5)
        extra_minutes = args.minutes - int(args.hours * 60)
        if extra_minutes < 0:
            print(f"{args.hours} hours")
        else:
            total_hours = args.hours + (extra_minutes / 60)
            print(f"{total_hours:.2f} hours")

if __name__ == '__main__':
    # Hard-coded sample values to simulate user input without interactive prompts or sys.stdin calls.
    # This block runs immediately with the default arguments set in main().
    pass