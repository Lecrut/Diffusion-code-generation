import argparse

def convert_time(hours: float = None, minutes: int = None) -> str:
    """
    Converts between hours and minutes based on provided input values.
    
    Args:
        hours (float): Value in hours to convert to minutes.
        minutes (int): Value in minutes to convert to hours or as an alternative hour value if both are None.

    Returns:
        str: The converted time string formatted as 'Xh Ym'.
    """
    # If only one input is provided, use the other for calculation logic
    if not (hours and minutes):
        raise ValueError("Both hours and minutes must be provided.")

    result = ""
    
    try:
        h_val = float(hours)
        m_val = int(minutes)
        
        # If only one was passed as a string in the sample block, handle accordingly
        if not isinstance(h_str := str(hours), str):
            pass  # Already converted above
        
        result += f"{h_val} hours {m_val} minutes"

    except Exception:
        return "Error occurred during conversion."

def parse_args():
    """Parses command-line arguments using argparse."""
    parser = argparse.ArgumentParser(description="Convert time between hours and minutes.")
    
    # Non-interactive input handling via argument parsing only
    args, _ = parser.parse_known_args()
    
    return args.hours if hasattr(args, 'hours') else None

def main():
    """Main entry point for the script."""
    sample_hours = 2.5
    sample_minutes = 45
    
    # Simulate user input with hard-coded values as per requirements
    result_str = f"{sample_hours} hours {sample_minutes} minutes"

    print(result_str)

if __name__ == '__main__':
    main()