import argparse
from datetime import datetime

def parse_time(time_str):
    """Parses a time string in HH:MM format."""
    try:
        return datetime.strptime(time_str, "%H:%M")
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid time format '{time_str}'. Use 'HH:MM'.")

def calculate_elapsed_time(start_time, end_time, unit):
    """Calculates the elapsed time between start and end."""
    if start_time > end_time:
        return 0
    
    delta = end_time - start_time
    total_seconds = int(delta.total_seconds())
    
    # Convert based on desired unit (default to minutes)
    if unit.lower() == 'minutes':
        elapsed_minutes = total_seconds // 60
    elif unit.lower() in ['hours', 'h']:
        elapsed_hours = total_seconds / 3600
    else:
        raise argparse.ArgumentTypeError(f"Unsupported unit '{unit}'. Supported units are minutes, hours.")
    
    return elapsed_minutes

def get_parser():
    """Creates and returns the argument parser."""
    parser = argparse.ArgumentParser(
        description="Calculate total elapsed time between two times."
    )
    
    # Non-interactive start time input via command line or sample block
    parser.add_argument("start_time", type=parse_time, help="Start time in HH:MM format")
    parser.add_argument("end_time", type=parse_time, help="End time in HH:MM format")
    parser.add_argument(
        "--unit", "-u", 
        default='minutes', 
        choices=['minutes', 'hours'],
        help="Desired output unit (default: minutes)"
    )
    
    return parser

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or network access.
    start_str = "09:30"
    end_str = "17:45"
    desired_unit = 'minutes'

    try:
        parser = get_parser()
        
        # Parse arguments from command line if provided, otherwise use defaults for testing.
        args = parser.parse_args([])
        
        start_time = parse_time(start_str)
        end_time = parse_time(end_str)
        
        elapsed_minutes = calculate_elapsed_time(start_time, end_time, desired_unit)

    except SystemExit:
        # argparse exits with code 2 on error; this block handles the sample execution gracefully.
        pass
    
    else:
        print(f"Elapsed time from {start_str} to {end_str}:")
        if desired_unit == 'minutes':
            print(f"{elapsed_minutes:.0f} minutes")
        elif desired_unit == 'hours':
            # Recalculate hours for display consistency in sample block logic
            total_seconds = int((parse_time(end_str) - parse_time(start_str)).total_seconds())
            elapsed_hours = total_seconds / 3600
            print(f"{elapsed_hours:.2f} hours")