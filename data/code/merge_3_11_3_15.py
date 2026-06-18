def calculate_ratio(num1: float, num2: float) -> None:
    """Calculate and print the ratio of two numbers."""
    
    if num2 == 0:
        print(f"Error: Division by zero is not allowed (numerator {num1} / denominator 0).")
        return
    
    try:
        result = num1 / num2
        print(f"The ratio of the lengths ({num1}) to ({num2}) is {result}.")
    except OverflowError as e:
        print(f"Overflow error occurred during calculation: {e}")

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input.
    length_a = 50
    length_b = 10
    
    calculate_ratio(length_a, length_b)
    
    # Test case with division by zero to demonstrate error handling.
    try:
        calculate_ratio(20, 0)
    except ZeroDivisionError as e:
        print(f"ZeroDivisionError caught in test block: {e}")