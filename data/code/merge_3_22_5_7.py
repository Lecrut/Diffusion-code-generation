def check_parity(number: int) -> str:
    """
    Determines if a given integer is odd or even.
    
    Args:
        number (int): The integer to evaluate.
        
    Returns:
        str: 'Odd' if the number is odd, 'Even' otherwise.
    """
    return "Odd" if number % 2 != 0 else "Even"

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements (no input() or sys.stdin)
    test_values = [1, -4, 5, 0]

    for val in test_values:
        result = check_parity(val)
        print(result)