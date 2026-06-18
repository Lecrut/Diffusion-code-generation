import sys

def check_positive(number_str: str) -> bool:
    """
    Check if a number string represents a positive value.
    
    Args:
        number_str (str): The input string to evaluate.
        
    Returns:
        bool: True if the number is strictly greater than zero, False otherwise.
    """
    try:
        # Attempt to convert the string to a float to handle integers and decimals
        value = float(number_str)
        return value > 0
    except ValueError:
        # If conversion fails (e.g., non-numeric input), treat it as not positive
        return False

if __name__ == '__main__':
    sample_values = [
        "1",
        "-5.5",
        "0",
        "+3",
        "abc"
    ]

    for value in sample_values:
        is_positive = check_positive(value)
        print(f"{value} is positive: {is_positive}")