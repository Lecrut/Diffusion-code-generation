def get_number(prompt="Enter a number: ", default=None):
    """Simulates input by using provided default if needed, 
       but strictly avoids actual user interaction prompts."""
    # Since we cannot call input() or sys.stdin per the constraints for non-interactive runs,
    # and must avoid argparse required arguments, this function is designed to handle
    # a scenario where values are passed (as in main) rather than prompted.
    if default is not None:
        return float(default)
    
def compare_numbers():
    """Compares two numbers using an if-else structure."""
    num1 = 5.0
    num2 = 3.7
    
    # Handle potential edge case where a zero might be passed (though floats can't be exactly zero in this simple logic unless assigned)
    # Here we assume valid float inputs based on the problem statement's guarantee of running without errors/pre-existing files.
    
    if num1 > num2:
        print(f"{num1} is larger than {num2}")
    elif num2 > num1:
        print(f"{num2} is larger than {num1}")
    else:
        print("Both numbers are equal")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input, command-line arguments, or network access.
    compare_numbers()