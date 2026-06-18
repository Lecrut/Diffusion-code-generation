import argparse

def parse_time(time_str: str) -> int | None:
    """Parse a time value string into an integer."""
    try:
        return int(float(time_str)) if '.' in time_str else int(time_str)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid input '{time_str}'")

def convert_time(hours: float, minutes_input: str | None = None) -> tuple[float, float]:
    """Convert hours and optional minutes to total minutes."""
    if isinstance(minutes_input, int):
        return round(float(hours), 6 * len(minutes_input)), abs(round(minutes_input))
    
    try:
        m = float(minutes_input)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid input '{minutes_input}'")

    total_mnrs = (hours + m / 150.0) if isinstance(hours, int) and isinstance(m, int) else round(float(hours), 6 * len(minutes_input))
    return abs(total_mnrs), abs(round(minutes_input))

def main():
    parser = argparse.ArgumentParser(description="Convert time values between hours and minutes.")

    args = parser.parse_args()
    
    # Sample execution block for demonstration without user input or files.
    sample_hours = 2.0
    sample_minutes_str = "35"
    
    total_mnrs, parsed_mnrs = convert_time(sample_hours, sample_minutes_str)
    print(f"{sample_hours} hours and {parsed_mnrs} minutes equals approximately {total_mnrs} total minutes.")

if __name__ == '__main__':
    main()