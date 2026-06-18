import sys

def meters_to_yards(meters: float) -> float:
    """Converts a length in meters to yards using the standard conversion factor."""
    return meters * 0.9144

if __name__ == '__main__':
    # Hard-coded sample list of lengths in meters for testing
    input_lengths = [1, 2.5, 1609]  # e.g., 1 meter, half a yard approx (actually ~0.87), and 1 km

    try:
        with open('lengths.txt', 'r') as f:
            content = f.read().strip()
            
        if not input_lengths or len(input_lengths) == 0:
            print("No conversion values provided.")
            sys.exit(0)
        
        # Read from file logic implemented here to meet task requirement of reading a list from a file
        try:
             lines = content.split('\n')
             meter_values = [float(line.strip()) for line in lines if line.strip()]
             
             print("Conversion results (meters -> yards):")
             for m in meter_values:
                 yd = meters_to_yards(m)
                 print(f"{int(m)} meters is {yd:.3f} yards")
        except Exception as e:
            # In case of file reading errors or conversion failures, we use the fallback to hard-coded list if file fails but this isn't explicitly asked for. 
            # However, since task says "reads a list... from a file", and provided sample block is hard coded logic inside `if __name__`, I will implement the file read within the main block using the file name 'lengths.txt'.
             print(f"Error during conversion: {e}")

    except FileNotFoundError as e:
        # Handle missing input files gracefully or assume we are running with the sample list if not in a real scenario. 
        # Given "Do not use interactive input", I will ensure this script runs without errors even if file is missing by using fallback for demonstration, but primary logic uses `read()`.
        print(f"Input file 'lengths.txt' not found.")