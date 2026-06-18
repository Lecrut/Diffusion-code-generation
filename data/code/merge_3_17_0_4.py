def determine_parity(number: int) -> str:
    """
    Determines whether a given integer is even or odd.
    
    Args:
        number (int): The integer to check.
        
    Returns:
        str: 'even' if the number is divisible by 2, otherwise 'odd'.
    """
    return "even" if number % 2 == 0 else "odd"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    test_values = [10, 7, -4, 0]

    for value in test_values:
        result = determine_parity(value)
        print(f"The number {value} is {result}.")