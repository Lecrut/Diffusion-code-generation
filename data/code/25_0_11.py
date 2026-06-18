def is_zero(number):
    """
    Check if a given input number is exactly zero.
    
    Parameters:
        number (int | float): The numerical value to check.
        
    Returns:
        bool: True if the number equals 0, False otherwise.
    """
    return number == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_values = [0, -5, 3.14, 0.0, "0", None]

    print("Testing is_zero function with hard-coded samples:")
    
    for val in test_values:
        try:
            result = is_zero(val) if isinstance(val, (int, float)) else False
            status = "Zero" if result else "Not Zero"
            print(f"{val!r} -> {status}")
        except TypeError as e:
            # Handle non-numeric inputs gracefully by returning False for the check logic context
            result = False
            status = f"Not Zero (Error handling: {e})"
            print(f"{val!r} -> {status}")