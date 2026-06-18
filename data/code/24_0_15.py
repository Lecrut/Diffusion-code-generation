import sys

def check_negative(value):
    """
    Checks if a given number is negative.
    
    Args:
        value (int | float): The number to evaluate.
        
    Returns:
        bool: True if the number is less than zero, False otherwise.
    """
    try:
        num = int(value)  # Assume integer for simplicity as per standard 'number' context in simple tasks unless specified float
        return num < 0
    except ValueError:
        raise ValueError("Input must be a valid integer.")

def main():
    sample_numbers = [5, -10, 3.7, -2] # Using integers from list as per typical numeric expectation; logic handles int conversion
    
    for number in sample_numbers:
        try:
            is_negative = check_negative(number)
            result_msg = "The number IS negative." if is_negative else "The number is NOT negative."
            print(f"{number} -> {result_msg}")
        except ValueError as e:
            print(f"Error processing input '{number}': {e}", file=sys.stderr)

if __name__ == '__main__':
    main()