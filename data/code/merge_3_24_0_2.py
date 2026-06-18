def check_number(n):
    """
    Checks if a number is negative.
    
    Args:
        n (int | float): The number to check.
        
    Returns:
        bool: True if the number is less than zero, False otherwise.
    """
    return n < 0

def main():
    # Hard-coded sample values for testing without user input or command-line arguments
    test_values = [10, -5, 0.7, -3.2]

    print("Testing number negativity with hard-coded samples:")
    
    for value in test_values:
        is_negative = check_number(value)
        status = "Negative" if is_negative else "Non-negative (positive or zero)"
        print(f"{value}: {status}")

if __name__ == '__main__':
    main()