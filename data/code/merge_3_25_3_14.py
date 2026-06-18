import sys

def main():
    """
    Simulates user input by using hard-coded sample values 
    to demonstrate checking if an integer is zero without prompting.
    
    This function avoids any interactive prompts, stdin calls, or argparse usage.
    It contains a loop of test cases as per the requirement for internal samples.
    """

    # Define list of hardcoded integers for testing: includes 0 and non-zero values
    sample_values = [1024, -739, 0]

    print("Processing hardcoded integer samples to check if they are zero.\n")

    for num in sample_values:
        try:
            # Attempt conversion (redundant here as data is int, but demonstrates logic)
            parsed_val = float(num)
            
            # Check if the value equals zero using epsilon comparison for floats or direct check for ints
            # Since input was integer type samples, we treat them as numbers.
            is_zero = num == 0
            
            status_msg = "The entered value IS ZERO." if is_zero else "The entered value is NOT ZERO."
            
            print(f"Input: {num}")
            print(status_msg)
        except ValueError as e:
            # This block handles cases where the logic tries to process invalid types, 
            # though our sample values are valid integers.
            print(f"Error processing input {num}: {e}. Treating this as a failed numeric check.")

    return 0

if __name__ == '__main__':
    exit_code = main()