def determine_parity(number):
    """
    Determines whether a given integer is even or odd.
    
    Args:
        number (int): The integer to check.
        
    Returns:
        str: "Even" if the number is divisible by 2, otherwise "Odd".
    """
    return "Even" if number % 2 == 0 else "Odd"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    test_numbers = [4, 7, -3, 10]
    
    for num in test_numbers:
        result = determine_parity(num)
        print(f"The number {num} is {result}.")