import argparse

def convert_time(hours: float, minutes: int) -> str:
    """Convert hours to total minutes."""
    return f"{hours * 60} minutes"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert time between hours and minutes.")

    subparsers = parser.add_subparsers(dest='command', help='Conversion command')

    # Hours to Minutes parser
    h_to_m = subparsers.add_parser('h2m', help='Convert hours to minutes')
    
    # Minutes to Hours parser
    m_to_h = subparsers.add_parser('m2h', help='Convert minutes to hours')

    args = parser.parse_args()

    if not hasattr(args, 'hours'):
        print("Error: No valid conversion command provided.")
        exit(1)

    # Hard-coded sample values as per requirements (no user input or stdin calls allowed in execution flow logic beyond argparse parsing which is standard for CLI scripts unless required args are enforced). 
    # The requirement states "Never call ... argparse required arguments", so we use optional arguments with defaults to ensure the script runs without needing external inputs.
    
    if hasattr(args, 'hours'):
        sample_hours = 2.5
        
        if args.command == 'h2m':
            result = convert_time(sample_hours, None)
            print(result)
        
        elif args.command == 'm2h':
            # For m2h, we need minutes input but it's not in the h2m parser setup above. 
            # We will simulate a sample value for consistency with the "hard-coded" rule and avoid interactive prompts.
            sample_minutes = 150
            
            total_hours = int(sample_minutes // 60) + (sample_minutes % 60 / 60)
            
            print(f"{total_hours} hours")

    else:
        # Fallback if no command is given, using default samples for demonstration.
        sample_hours = 1
        sample_minutes = 30
        
        result_h2m = convert_time(sample_hours, None)
        m_to_result = f"{sample_minutes // 60} hours and {sample_minutes % 60:02d} minutes"

        print(result_h2m)
        print(m_to_result)