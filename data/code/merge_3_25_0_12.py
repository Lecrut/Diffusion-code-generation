def is_zero(number):
    """
    Check if a given input number is exactly zero.
    
    Parameters:
        number (int, float): The numerical value to check.
        
    Returns:
        bool: True if the number is 0, False otherwise.
    """
    return number == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_values = [0, -1, 1, 3.5, 0.0, float('inf'), None]

    print("Testing is_zero function:")
    for value in test_values:
        result = is_zero(value) if isinstance(value, (int, float)) else "Invalid type"
        status = "Zero detected!" if result and not isinstance(value, bool) else ""
        print(f"is_zero({value}) -> {result} {status}")