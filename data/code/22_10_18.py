import sys

def check_parity(number: int) -> None:
    """
    Determines whether a given integer is odd or even using the modulo operator.
    
    Args:
        number (int): The integer to be checked.
        
    Returns:
        None
        
    Raises:
        TypeError: If 'number' is not an integer instance.
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")

    # Use modulo operator for efficient parity check
    remainder = number % 2
    
    if remainder == 0:
        status = "even"
    else:
        status = "odd"
        
    print(f"{number} is {status}.")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    samples = [1, 2, -3, 0]

    for num in samples:
        check_parity(num)