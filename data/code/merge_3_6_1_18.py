def calculate_weight_difference(a: float, b: float) -> float:
    """
    Calculate the absolute difference between two floating-point numbers.
    
    This function uses Python's built-in abs() and subtraction operators,
    which are implemented in C for maximum efficiency on modern interpreters.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The absolute difference between a and b.
    """
    return abs(a - b)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    value1 = 3.50789
    value2 = 4.12345

    result = calculate_weight_difference(value1, value2)
    
    print(f"Absolute difference: {result}")