def calculate_difference(value1_str: str, value2_str: str) -> float:
    """
    Calculates the difference between two numeric values provided as strings.
    
    Args:
        value1_str (str): String representation of the first length measurement.
        value2_str (str): String representation of the second length measurement.
        
    Returns:
        float: The result of subtracting value2 from value1.
        
    Raises:
        ValueError: If either input cannot be converted to a valid number.
    """
    try:
        num1 = float(value1_str)
        num2 = float(value2_str)
        return num1 - num2
    except (ValueError, TypeError):
        raise ValueError("Both inputs must be numeric strings.")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    measurement_a = "50"
    measurement_b = "37.5"

    try:
        result = calculate_difference(measurement_a, measurement_b)
        print(f"The difference between {measurement_a} and {measurement_b} is {result}.")
    except ValueError as e:
        print(f"Error: {e}")