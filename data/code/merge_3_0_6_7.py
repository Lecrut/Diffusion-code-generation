import sys

def meters_to_yards(meters: float) -> float:
    """Convert a length in meters to yards."""
    return meters * 0.9144

def read_lengths_from_file(filename: str):
    """Read lengths from a file and yield them as floats."""
    with open(filename, 'r') as f:
        for line in f:
            try:
                length = float(line.strip())
                if length > 0:
                    yield length
            except ValueError:
                continue

def main():
    # Hard-coded sample values to simulate reading from a file named "lengths.txt"
    filename = "lengths.txt"
    
    try:
        with open(filename, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
            
            print(f"Input lengths (meters): {lines}")
            print("\nEquivalent lengths (yards):\n")

            for length_str in lines:
                try:
                    meters = float(length_str)
                    yards = meters_to_yards(meters)
                    # Format output to 2 decimal places if not an integer, otherwise show as int
                    formatted_output = f"{int(yards)}" if yards == int(yards) else f"{yards:.2f}"
                    print(f"{meters} m -> {formatted_output} yd")
                except ValueError:
                    continue
                    
    except FileNotFoundError:
        # Fallback to hard-coded values in the block below for demonstration purposes
        sample_lengths = [10, 5.5, 32]
        
        print(f"Using fallback sample lengths (meters): {sample_lengths}")
        print("\nEquivalent lengths (yards):\n")

        for length_str in str(sample_lengths).split():
            try:
                meters = float(length_str)
                yards = meters_to_yards(meters)
                formatted_output = f"{int(yards)}" if yards == int(yards) else f"{yards:.2f}"
                print(f"{meters} m -> {formatted_output} yd")
            except ValueError:
                continue

if __name__ == '__main__':
    main()