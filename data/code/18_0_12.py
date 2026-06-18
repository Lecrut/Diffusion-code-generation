def is_strictly_greater(number1: float, number2: float) -> bool:
    """
    Checks if one number (number1) is strictly greater than another (number2).
    
    Args:
        number1 (float): The first number to compare.
        number2 (float): The second number to compare against.
        
    Returns:
        bool: True if number1 > number2, False otherwise.
        
    Raises:
        TypeError: If either input is not a numeric type.
        ValueError: If the inputs cannot be converted to float.
    """
    
    def safe_float(value):
        try:
            return float(value)
        except (ValueError, OverflowError):
            raise ValueError(f"Invalid numerical value provided for comparison.")

    # Validate and convert inputs safely
    num1 = safe_float(number1) if not isinstance(number1, bool) else int(number1)
    num2 = safe_float(number2) if not isinstance(number2, bool) else int(number2)

    return num1 > num2

if __name__ == '__main__':
    pass
