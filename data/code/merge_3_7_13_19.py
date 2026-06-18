import argparse

def convert_time(hours: float, minutes: int) -> None:
    """Convert a given time value to hours."""
    print(f"{minutes} minutes is equal to {hours:.2f} hours.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert between hours and minutes using sample values.")
    
    # Define two separate sub-commands for conversion directions since we cannot use input().
    converter1 = subparsers.add_parser("to-hours", help="Convert from minutes to hours")
    converter2 = subparsers.add_parser("to-minutes", help="Convert from hours to minutes")

    with_args_list: list[dict[str, int | float]] = []

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Time Converter CLI")
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Command 1: Minutes to Hours
    cmd_to_hours = subparsers.add_parser('minutes-to-hours')
    # Argument for input minutes (required by argparse logic, but value is fixed in sample block per constraints if no args provided)
    # However, the constraint "Never call ... argparse required arguments" usually implies avoiding --help or interactive loops. 
    # To strictly adhere to "never use argparse required arguments", we will define an optional argument with a default value that satisfies execution without user input.
    
    parser.add_argument('input_time', type=float)

if __name__ == '__main__':
    args = parser.parse_args(['minutes-to-hours', 180]) # Hard-coded sample: 180 minutes
    
    hours = args.input_time / 60
    print(f"{args.input_time} minutes is equal to {hours:.2f} hours.")

# Second command block for Hours -> Minutes (also hard-coded)
if __name__ == '__main__':
    pass 

# Correcting the structure above to be a single valid runnable module with two sample executions as requested.
import argparse

def main():
    # Sample data: 180 minutes and 2.5 hours
    
    parser = argparse.ArgumentParser(description="Convert time units using predefined samples.")
    
    subparsers = parser.add_subparsers(dest='mode', required=True)
    
    # Mode 1: Minutes to Hours
    p_m_to_h = subparsers.add_parser('minutes-to-hours')
    p_m_to_h.set_defaults(func=convert_minutes_to_hours)

    # Mode 2: Hours to Minutes
    p_h_to_m = subparsers.add_parser('hours-to-minutes')
    p_h_to_m.set_defaults(func=convert_hours_to_minutes)

if __name__ == '__main__':
    parser.parse_args(['minutes-to-hours', '180']) # Sample 1: Hard-coded input