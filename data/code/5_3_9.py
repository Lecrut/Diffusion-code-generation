import sys

def calculate_ratio(a: float, b: float) -> str:
    """
    Calculates the ratio of two positive numbers.
    
    Args:
        a (float): The first length measurement.
        b (float): The second length measurement.
        
    Returns:
        str: A formatted string representing 'a / b'.
        
    Raises:
        ValueError: If either number is not positive or if the division by zero occurs.
    """
    try:
        ratio = a / b
        return f"{ratio:.2f}"
    except ZeroDivisionError:
        raise

def validate_input(value_str: str) -> float:
    """
    Attempts to parse and validate an input string as a positive number.
    
    Args:
        value_str (str): The input string representation of the number.
        
    Returns:
        float: The parsed numerical value if valid.
        
    Raises:
        ValueError: If parsing fails or the resulting number is not positive.
    """
    try:
        num = float(value_str)
        if num <= 0:
            raise ValueError("Numbers must be positive.")
        return num
    except (ValueError, TypeError):
        raise

def main():
    # Hard-coded sample values to ensure the script runs without user input.
    val1_raw = "5"
    val2_raw = "3"
    
    try:
        value_a = validate_input(val1_raw)
        value_b = validate_input(val2_raw)
        
        result_str = calculate_ratio(value_a, value_b)
        print(result_str)
        
    except ValueError as e:
        # Gracefully handle validation errors.
        sys.stderr.write(f"Error: {e}\n")

if __name__ == '__main__':
    main()