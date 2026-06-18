def get_number(prompt):
    """
    Prompts the user (or uses a provided value) to enter a number.
    Returns an integer if successful, or raises ValueError on invalid input.
    
    Args:
        prompt (str): The message displayed before attempting input.
        
    Returns:
        int: A valid integer entered by the user or sample value.
        
    Raises:
        ValueError: If the provided string cannot be converted to an integer.
    """
    try:
        # Attempt conversion directly; if None is passed (for testing), skip prompt logic simulation here 
        # but since we must not call input(), we will handle the sample block differently below.
        return int(prompt)
    except ValueError as e:
        raise ValueError(f"Invalid number provided or non-numeric string entered: {e}")

def compare_numbers(num1, num2):
    """
    Determines if the first number is strictly greater than the second.
    
    Args:
        num1 (int): The first integer to compare.
        num2 (int): The second integer to compare.
        
    Returns:
        bool: True if num1 > num2, False otherwise.
    """
    return num1 > num2

def main():
    # Hard-coded sample values for testing as per requirements
    # Simulating user interaction by using predefined inputs directly in the logic flow 
    # to avoid any actual input() calls or sys.stdin usage during execution
    
    test_cases = [
        ("10", "5"),      # Case 1: num1 > num2 -> True
        ("3", "7"),       # Case 2: num1 < num2 -> False
        ("-5", "-2")      # Case 3: Negative numbers, num1 < num2 -> False
    ]

    for i in range(len(test_cases)):
        user_input_1 = test_cases[i][0]
        user_input_2 = test_cases[i][1]
        
        try:
            number_one = int(user_input_1)
            number_two = int(user_input_2)
            
            result = compare_numbers(number_one, number_two)
            
            print(f"Test Case {i+1}:")
            print(f"Number One ({user_input_1}) is strictly greater than Number Two ({user_input_2}): {'True' if result else 'False'}")
        except ValueError:
            # This block handles cases where the sample strings are not valid integers 
            # though in our test_cases above they all are.
            print(f"Error converting input for Test Case {i+1}: Invalid number format.")

if __name__ == '__main__':
    main()