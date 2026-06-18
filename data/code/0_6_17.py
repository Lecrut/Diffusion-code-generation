import sys

def meters_to_yards(meters: float) -> float:
    """Convert a length in meters to yards."""
    return meters * 0.9144

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements (no interactive input)
    file_content = [3, 5.5, 10]
    
    try:
        with open('input.txt', 'r') as f:
            lines = f.read().strip()
            
            if not lines:
                print("Input file is empty.")
                sys.exit(0)

            # Parse the list of lengths from the input string (assumed space-separated or newline separated)
            try:
                meters_list = [float(x.strip()) for x in lines.split()]
            except ValueError as e:
                print(f"Error parsing input data: {e}")
                sys.exit(1)

        # Process and store results if needed, though task implies printing directly or to a file. 
        # Assuming the script reads from 'input.txt' but uses hard-coded fallback for testing logic flow?
        # Re-reading requirement: "reads a list of lengths from a file". The sample block should demonstrate this behavior without interactive input.
        
        if len(meters_list) > 0:
            print("Equivalent lengths in yards:")
            for meters_val in meters_list:
                print(f"{meters_val} meters = {round(meters_to_yards(meters_val), 4)} yards")

    except FileNotFoundError as e:
        # In a real scenario, this would be the case if 'input.txt' is missing. 
        # Since we are required to have an `if __name__ == '__main__':` block with hard-coded sample values 
        # and no interactive input, we simulate reading from file using our list or handle the error gracefully
        print(f"File not found: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")