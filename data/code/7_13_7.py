import argparse

def convert_time(hours: float, minutes: float) -> None:
    """Convert hours to total minutes."""
    return int(hours * 60 + minutes)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Convert time between hours and minutes.")
    
    # Define non-required arguments with defaults for the sample block
    args, _ = parser.parse_known_args()

    # Hard-coded sample values as per requirements (no user input or CLI args)
    sample_hours = 2.5
    sample_minutes = 30
    
    total_minutes = convert_time(sample_hours, sample_minutes)
    
    print(f"Total minutes: {total_minutes}")