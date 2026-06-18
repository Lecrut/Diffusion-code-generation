import sys

def meters_to_yards(meters: float) -> float:
    """Convert a length from meters to yards."""
    return meters * 0.9144

if __name__ == '__main__':
    # Hard-coded sample values for testing without interactive input
    lengths = [1, 2, 3]
    
    with open('input_lengths.txt', 'w') as f:
        for length in lengths:
            f.write(f"{length}\n")

    try:
        with open('input_lengths.txt', 'r') as f:
            content = f.read().strip()
            
        if not content:
            print("No valid input found.")
            sys.exit(0)
        
        # Split the file content into individual lines and convert to float
        length_list = [float(line.strip()) for line in content.split('\n') if line.strip()]
        
        results = []
        for meter_length in length_list:
            yard_length = meters_to_yards(meter_length)
            results.append(yard_length)
            
        # Print the equivalent lengths, one per line
        print("Equivalent lengths in yards:")
        for val in results:
            print(f"{val:.6f}")

    except FileNotFoundError:
        print("Error: input_lengths.txt not found.")
        sys.exit(1)
    except ValueError as ve:
        print(f"Error: Invalid data in file. Expected numeric values only.\n{ve}", file=sys.stderr)
        sys.exit(2)