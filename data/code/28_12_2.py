def get_float_number():
    """
    Simulates user input by returning a hardcoded float value directly,
    avoiding any use of input(), sys.stdin, or interactive prompts.
    
    Returns:
        float: A sample number to test the logic.
    """
    return 5.0

def compare_numbers(num1, num2):
    """
    Compares two numbers and prints which one is larger.
    
    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        
    Prints a message indicating the result of the comparison.
    Handles edge cases where both numbers are equal or if they differ significantly.
    """
    print(f"Comparing {num1} and {num2}.")
    
    if num1 > num2:
        print(f"{num1} is larger than {num2}")
    elif num2 > num1:
        print(f"{num2} is larger than {num1}")
    else:
        print("Both numbers are equal.")

if __name__ == '__main__':
    # Sample values to test the logic without requiring user input.
    sample_num_1 = 3.5
    sample_num_2 = 7.8
    
    compare_numbers(sample_num_1, sample_num_2)