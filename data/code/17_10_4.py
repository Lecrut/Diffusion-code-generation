import sys

def check_parity(number: int) -> None:
    """
    Determines if a number is even or odd using the modulo operator.
    
    Args:
        number (int): The integer to evaluate
        
    Returns:
        None: Prints the result directly
    """
    if number % 2 == 0:
        print(f"{number} is Even")
    else:
        print(f"{number} is Odd")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    test_numbers = [1, 2, -3, 4]

    for num in test_numbers:
        check_parity(num)