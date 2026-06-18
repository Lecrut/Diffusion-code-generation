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

if __name__ == '__main__':
    # Hard-coded sample values to simulate reading from a file named 'lengths.txt'
    input_data = [1.6, 3.28, 54.87]
    
    try:
        with open('lengths.txt', 'r') as f:
            lines = f.readlines()
        
        # Filter out empty lines and convert to float
        valid_lengths = []
        for line in lines:
            if line.strip():
                try:
                    val = float(line.strip())
                    if val > 0:
                        valid_lengths.append(val)
                except ValueError:
                    continue
        
        # If file reading fails or is empty, use sample data as fallback
        if not valid_lengths and input_data:
            print("Using sample values since no valid lengths were found in the file.")
            for val in input_data:
                yards = meters_to_yards(val)
                print(f"{val} meters = {yards:.2f} yards")
        
        else:
            # Process actual data from file or fallback to samples if needed
            all_lengths = valid_lengths + [x for x in input_data if not any(abs(x - y) < 1e-9 for y in valid_lengths)]
            
            print("Converting lengths from meters to yards:")
            for length in all_lengths:
                yards = meters_to_yards(length)
                print(f"{length} meters = {yards:.2f} yards")

    except FileNotFoundError:
        # Fallback if the file doesn't exist, use sample data directly
        print("File 'lengths.txt' not found. Using sample values.")
        for length in input_data:
            yards = meters_to_yards(length)
            print(f"{length} meters = {yards:.2f} yards")