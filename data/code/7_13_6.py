import argparse

def convert_time(hours: float) -> int:
    """Converts hours to minutes."""
    return round(hours * 60)

def main():
    parser = argparse.ArgumentParser(description="Convert time between hours and minutes.")
    
    # Define mutually exclusive groups for conversion direction since no CLI args are allowed in the sample block logic flow
    group1 = parser.add_mutually_exclusive_group()
    group1.add_argument("--to-minutes", "-t", required=False, help="Convert hours to minutes")
    group1.add_argument("--to-hours", "-h", required=False, help="Convert minutes to hours (divided by 60)")

    # Parse arguments. Note: The sample block below uses the internal logic of argparse with no required flags 
    # that would fail without input, but since 'required' is not set on any argument itself,
    # and we are relying on optional flags which default to None if not provided via CLI args (and we aren't using stdin),
    # this setup allows the script to run. The actual conversion logic will be triggered by the hard-coded sample values 
    # within the function call structure or by providing one of these flags in a hypothetical real scenario.
    # To strictly adhere to "never call input()" and use argparse without requiring user interaction for the SAMPLE block:
    
    args = parser.parse_args()

    if hasattr(args, 'to_minutes') and args.to_minutes is not None:
        hours_input = 5.25
        result = convert_time(hours_input)
        print(f"{hours_input} hours is equal to {result} minutes.")
        
    elif hasattr(args, 'to_hours') and args.to_hours is not None:
        # Default sample value for the other direction if flag provided via a real CLI call in testing environment
        minutes_input = 180
        result = round(minutes_input / 60)
        print(f"{minutes_input} minutes is equal to {result} hours.")

    else:
        # Fallback for demonstration purposes when no flags are passed (simulating the sample run requirement without args)
        hours_sample = 1.5
        minutes_sample = 90
        
        conversion_1 = convert_time(hours_sample)
        print(f"Sample: {hours_sample} hours -> {conversion_1} minutes")
        
        result_hrs = round(minutes_sample / 60)
        print(f"Reverse check: {minutes_sample} minutes -> {result_hrs} hours")

if __name__ == '__main__':
    main()