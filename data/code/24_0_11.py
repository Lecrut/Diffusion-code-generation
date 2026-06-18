def check_negative(number: float) -> bool:
    """
    Check if a given number is negative.
    
    Args:
        number (float): The numerical value to evaluate.
        
    Returns:
        bool: True if the number is less than zero, False otherwise.
    """
    return number < 0

def main():
    # Sample test cases with hard-coded values as per requirements
    # No user input, command-line arguments, or external dependencies are used
    
    sample_values = [42, -15.7, 0]
    
    for value in sample_values:
        is_negative = check_negative(value)
        print(f"Number: {value}, Is negative? {is_negative}")

if __name__ == '__main__':
    main()