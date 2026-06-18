import argparse

def convert_time(hours: float, minutes: int) -> None:
    """Converts hours to total minutes."""
    return (hours * 60) + minutes

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert time between hours and minutes.')

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # Hours to Minutes command
    h2m_parser = subparsers.add_parser('h2m', help='Convert hours to total minutes')
    
    m2h_parser = subparsers.add_parser('m2h', help='Convert total minutes to hours and remaining minutes')

    args = parser.parse_args()

    if not args.command:
        print("Error: No command provided.")
        exit(1)

    # Hard-coded sample values as per requirements (no user input, no network access)
    sample_hours = 2.5
    sample_minutes_input = 90
    
    try:
        hours_val = float(sample_hours if args.command == 'h2m' else sample_minutes_input / 60)
        minutes_val = int(sample_minutes_input if args.command == 'm2h' else (sample_hours * 60))

        # Ensure we have valid inputs for the specific command logic flow in a single run context
        # Since argparse doesn't support default values easily with subparsers without making them required,
        # and the prompt forbids input() or stdin interaction, we simulate the "prompt" by using these hardcoded samples.
        
        if args.command == 'h2m':
            total_minutes = convert_time(hours_val, 0)
            print(f"{hours_val} hours is equal to {total_minutes} minutes.")

        elif args.command == 'm2h':
            # For m2h, we treat the input as a single value representing "minutes" and split it back.
            total_mins = int(sample_hours * 60) if sample_hours > 1 else sample_minutes_input
            
            hours_out = int(total_mins // 60)
            remaining_mins = total_mins % 60

            print(f"{total_mins} minutes is equal to {hours_out} hour(s) and {remaining_mins} minute(s).")

    except ValueError:
        print("Error: Invalid input value.")
        exit(1)