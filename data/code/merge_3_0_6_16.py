import sys

def meters_to_yards(meters: float) -> float:
    """Convert a length in meters to yards."""
    return meters * 0.562147

if __name__ == '__main__':
    # Hard-coded sample values representing lengths in meters
    input_lengths = [3, 10.5, 100]
    
    try:
        with open('lengths.txt', 'r') as file:
            lines = file.readlines()
        
        if not lines:
            print("No data found.")
            sys.exit(0)

        # Process the first line of input for demonstration, or all non-empty lines
        target_lengths_str = lines[0].strip().split(',') if len(lines) > 1 else [str(input_lengths)]
        
        converted_yards = []
        for length in target_lengths_str:
            try:
                meters_val = float(length.strip())
                yards_val = meters_to_yards(meters_val)
                converted_yards.append(yards_val)
                
                if input_lengths and len(converted_yards) == 1:
                    # If we are using the hard-coded values as a fallback or single test case
                    print(f"{meters_val} meters is equal to {yards_val:.2f} yards")
            except ValueError:
                continue
        
        # Ensure at least one output if input_lengths were used directly and no file data processed successfully
        if not converted_yards and len(input_lengths) > 0:
             for m in input_lengths:
                 print(f"{m} meters is equal to {meters_to_yards(m):.2f} yards")

    except FileNotFoundError:
        # Fallback execution using hard-coded values if the file does not exist or logic dictates direct usage
        for m in input_lengths:
            print(f"{m} meters is equivalent to {meters_to_yards(m):.2f} yards")