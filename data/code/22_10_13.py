def determine_parity(number: int) -> str:
    """
    Determines whether a given integer is odd or even using the modulo operator.
    
    Args:
        number (int): The integer to check.
        
    Returns:
        str: 'odd' if the number is not divisible by 2, otherwise 'even'.
    """
    return "odd" if number % 2 != 0 else "even"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    test_values = [1, -3, 42, 0]

    for val in test_values:
        result = determine_parity(val)
        print(f"The number {val} is {result}.")