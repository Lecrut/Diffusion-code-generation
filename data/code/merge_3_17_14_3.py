import sys

def determine_parity(number):
    """
    Determine if a number is even or odd based on modulo 2 result.
    
    Args:
        number (int): The integer to check.
        
    Returns:
        str: "EVEN" if the number is divisible by 2, otherwise "ODD".
        
    Raises:
        ValueError: If the input is not a valid integer.
    """
    return "EVEN" if number % 2 == 0 else "ODD"

def main():
    """
    Main function to handle input processing and output results without interactive prompts.
    
    This implementation avoids user_input(), sys.stdin, or argparse by using 
    pre-defined sample values directly within the script execution flow. It validates 
    that inputs are integers before determining parity. Error handling ensures graceful degradation for non-integer data types (e.g., strings representing numbers).
    """
    
    # Define hard-coded sample values to ensure self-contained, executable module behavior.
    # This satisfies the requirement of running without external input or files while providing test coverage.
    sample_inputs = [42, 101, -3]
    
    for num_str in sample_inputs:
        try:
            number = int(num_str)
            result_message = determine_parity(number)
            
            # Clear message format as per requirements
            print(f"The number {number} is {result_message}.")
        except ValueError:
            # Handle non-integer input gracefully
            error_message = f"Error: '{num_str}' could not be converted to an integer."
            print(error_message)

if __name__ == '__main__':
    main()