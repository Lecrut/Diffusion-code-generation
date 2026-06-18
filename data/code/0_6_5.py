import sys

def meters_to_yards(meters: float) -> float:
    """Convert a length in meters to yards."""
    return meters * 0.56214

if __name__ == '__main__':
    # Hard-coded sample values for testing, simulating reading from a file line by line
    input_lengths = [
        "3",       # Example: 3 meters
        "175",     # Example: 175 meters (approximate running track length)
        "0.25"     # Example: 0.25 meters
    ]

    for line in input_lengths:
        try:
            meter_value = float(line.strip())
            yard_value = meters_to_yards(meter_value)
            print(f"{meter_value} meters is approximately {yard_value:.4f} yards")
        except ValueError:
            # Skip lines that are not valid numbers to handle potential file noise gracefully
            continue