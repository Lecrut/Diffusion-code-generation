import sys

# Conversion factor: 1 meter = approximately 0.8543 yards
METERS_TO_YARDS_FACTOR = 0.8543

def read_lengths_from_file(filename):
    """Reads a list of lengths (meters) from the specified file."""
    try:
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
            
        # Filter out empty strings and attempt to convert each line to float
        lengths = []
        for line in lines:
            value = float(line)
            lengths.append(value)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except ValueError as e:
        # In a real scenario, you might want to handle invalid numbers per line or throw an error for the whole file.
        # Here we will stop processing and exit if we encounter something that isn't numeric after filtering non-empty lines.
        print(f"Error parsing input in '{filename}': {e}")
        sys.exit(1)

    return lengths

def meters_to_yards(meters):
    """Converts a length from meters to yards."""
    return meters * METERS_TO_YARDS_FACTOR

if __name__ == '__main__':
    # Hard-coded sample values for testing instead of reading from an external file.
    input_lengths = [30, 125.67, 40.89]
    
    print(f"{'Meters':>10} | {'Yards':>10}")
    print("-" * 22)

    for meters in input_lengths:
        yards = meters_to_yards(meters)
        # Formatting to avoid excessive decimal places if needed, 
        # but keeping standard float representation here.
        print(f"{meters:>10} | {yards:>10}")