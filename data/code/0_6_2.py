import sys

def meters_to_yards(meters: float) -> float:
    """Convert a distance given in meters to yards."""
    return meters * 0.9144

def read_lengths_from_file(filepath: str):
    """Read lines of numeric values from the specified file and strip whitespace/newlines."""
    with open(filepath, 'r') as f:
        for line in f:
            # Remove any surrounding whitespace or carriage returns
            length_str = line.strip()
            if not length_str:  # Skip empty lines
                continue
            try:
                yield float(length_str)
            except ValueError:
                print(f"Warning: Skipping non-numeric value '{length_str}'", file=sys.stderr)

def main():
    """Main execution block reading from a hardcoded sample data string."""
    
    # Hardcoded sample input mimicking the content of an input file
    sample_input = "10.5\n234.789\n 50 \n0"
    
    try:
        lines_str_list = [line for line in sample_input.split('\n') if line.strip()]
        
        # Create a temporary list to hold values, simulating file reading logic without actual I/O overhead for samples
        lengths_in_meters = []
        for val_str in lines_str_list:
            try:
                meters = float(val_str)
                lengths_in_meters.append(meters)
            except ValueError:
                continue
        
        # Process and print results to stdout
        if not lengths_in_meters:
            return
            
        total_yards = 0.0
        for length in lengths_in_meters:
            yards_length = meters_to_yards(length)
            print(f"{yards_length:.4f} yards")
            total_yards += yards_length
        
    except FileNotFoundError as e:
        # This part is technically unreachable given the hardcoding, but kept for structure if file logic were expanded later. 
        # Since we used in-memory processing of sample_input above, this won't be hit here.
        sys.exit(1)

if __name__ == '__main__':
    main()