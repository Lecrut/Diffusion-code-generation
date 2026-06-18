import sys

def is_odd_or_even(number: int) -> str:
    """
    Determines if a given integer is odd or even using the modulo operator.

    Args:
        number (int): The integer to check.

    Returns:
        str: A string indicating whether the number is 'odd' or 'even'.
    """
    remainder = number % 2
    
    # Efficiency note: Using modulo (%) directly avoids unnecessary branching logic overhead,
    # as it performs a single arithmetic operation which CPU architectures optimize well.
    if remainder == 0:
        return "The number is even."
    else:
        return "The number is odd."

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input,
    # command-line arguments, network access, or pre-existing files.
    
    test_cases = [10, 7, -3, 0]

    for num in test_cases:
        result = is_odd_or_even(num)
        print(f"Number {num}: {result}")