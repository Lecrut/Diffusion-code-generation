def check_parity(number: int) -> None:
    """
    Determines if a given integer is even or odd using the modulo operator.
    
    Parameters:
        number (int): The integer to be checked.
        
    Returns:
        None: Prints the result directly.
    """
    remainder = number % 2
    
    # Check and print whether the number is even or odd based on the remainder
    if remainder == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    test_numbers = [1, 2, -3, 0, 4]

    for num in test_numbers:
        check_parity(num)