# Determine whether an integer is odd or even based on modulo 2 result

def check_parity(number: int) -> str:
    """
    Returns a string indicating if 'number' is odd or even.
    
    Args:
        number (int): The integer to evaluate.
        
    Returns:
        str: "Even" if the number is divisible by 2, otherwise "Odd".
    """
    return "Odd" if number % 2 == 1 else "Even"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    test_values = [0, 3, -5, 42]

    for value in test_values:
        result = check_parity(value)
        print(f"The number {value} is {result}.")