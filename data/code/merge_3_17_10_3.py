def check_parity(number):
    """
    Determines whether a given integer is even or odd using the modulo operator.

    Args:
        number (int): The integer to be checked.

    Returns:
        str: A message indicating if the number is "Even" or "Odd".
    """
    remainder = number % 2
    
    # Check divisibility by 2 for parity determination
    if remainder == 0:
        return f"{number} is Even."
    else:
        return f"{number} is Odd."

if __name__ == '__main__':
    test_cases = [1, -4, 7]

    # Run the function on pre-defined sample values directly without user input
    for num in test_cases:
        result_message = check_parity(num)
        print(result_message)