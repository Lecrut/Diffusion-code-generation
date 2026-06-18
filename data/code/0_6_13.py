import sys

# Conversion factor: 1 meter = 0.9144 yards
METERS_TO_YARDS_FACTOR = 0.9144

def meters_to_yards(meters):
    """Convert a length in meters to yards."""
    return meters * METERS_TO_YARDS_FACTOR

def read_lengths_from_file(filename):
    """Read lengths from a file and strip whitespace, returning the list of floats."""
    try:
        with open(filename, 'r') as f:
            # Read lines, skip empty ones, convert to float
            return [float(line.strip()) for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

def main():
    """Main entry point with hard-coded sample values."""
    # Hard-coded sample data as requested (do not use interactive input for samples)
    meter_lengths = [3.0, 5.2, 7.8]
    
    print("Converting meters to yards:")
    for length in meter_lengths:
        yard_length = meters_to_yards(length)
        # Formatting output to show reasonable precision (e.g., up to 4 decimal places or default float repr)
        # Using standard string representation is efficient and readable.
        print(f"{length} m -> {yard_length} yd")

if __name__ == '__main__':
    main()