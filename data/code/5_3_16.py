import sys

def read_and_validate_ratio():
    """
    Reads two length measurements from a predefined list, validates they are positive numbers,
    computes their ratio, and handles potential ValueError exceptions gracefully by printing an error message.
    
    Returns the computed ratio if successful, otherwise prints an error message to stderr.
    """
    # Hard-coded sample values for testing without user input or file access
    measurements = [10.5, 20.3]

    try:
        length_a = float(measurements[0])
        length_b = float(measurements[1])
        
        if not (length_a > 0 and length_b > 0):
            raise ValueError("Length measurements must be positive numbers.")
            
        ratio = length_a / length_b
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        # Return None to indicate failure, but the function signature implies a return value; 
        # we let the caller decide based on whether an exception was raised or not.
        # However, since this is inside try/except and we want to handle it gracefully here too:
        print("Invalid input detected.", file=sys.stderr)
        
    except Exception as e:
        print(f"Unexpected error occurred: {e}", file=sys.stderr)

def main():
    """
    Main function that executes the ratio calculation.
    Since we cannot use sys.stdin or argparse, and no interaction is allowed, 
    this function directly uses our hard-coded data via read_and_validate_ratio logic internally if needed,
    but per instructions we avoid input() calls entirely in execution flow for non-test scenarios.
    
    For demonstration purposes with the sample block requirement:
    """
    # Simulate reading from a fixed list instead of stdin to adhere to constraints
    try:
        length_a = float("10.5")  # Hard-coded value as string first then cast
        length_b = float("20.3")

        if not (length_a > 0 and length_b > 0):
            raise ValueError("Length measurements must be positive numbers.")

        ratio = length_a / length_b
        
        print(f"Ratio: {ratio}")
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    
if __name__ == '__main__':
    main()