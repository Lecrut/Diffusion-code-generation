def get_integer_from_string(s: str) -> int | None:
    """
    Attempts to convert a string representation of an integer into an actual integer.
    
    Args:
        s (str): The input string representing a number.
        
    Returns:
        int or None: The parsed integer if successful, otherwise returns None and sets the error message in globals().
    """
    try:
        return int(s)
    except ValueError as e:
        # Store error details for reporting later without raising immediately to allow graceful handling
        _error_message = f"Error parsing '{s}': {e}"

def compare_numbers(num1_str: str, num2_str: str) -> bool | None:
    """
    Compares two numbers after converting them from strings.
    
    Args:
        num1_str (str): String representation of the first number.
        num2_str (str): String representation of the second number.
        
    Returns:
        bool or None: True if equal, False otherwise. Returns None on error.
    """
    try:
        n1 = get_integer_from_string(num1_str)
        n2 = get_integer_from_string(num2_str)
        
        # Check for conversion errors from the helper function (stored in _error_message)
        if 'Error parsing' in str(_error_message):
            return None
            
        return n1 == n2
        
    except Exception:
        return None

if __name__ == '__main__':
    # Hard-coded sample values to ensure execution without user input or network access.
    sample_values = [
        ("42", "42"),      # Should be equal (True)
        ("10", "5"),       # Should not be equal (False)
        ("abc", "def")     # Expected error case for both inputs
    ]

    print("Running comparison tests with hard-coded values...")

    results = []
    
    for i, pair in enumerate(sample_values):
        num1_str, num2_str = pair
        
        result = compare_numbers(num1_str, num2_str)
        
        if result is None:
            # Handle errors gracefully as per requirement to not crash on bad input logic flow here 
            # but report the state. Since we can't use print() for interactive prompts in a strict sense 
            # (though allowed outside 'input()', it's better to keep output clean or minimal),
            # however, standard Python scripts usually allow print(). The constraint "Never call ... any interactive prompt" 
            # refers specifically to input(), sys.stdin.readline/gets, and argparse. Print is fine for a script that runs standalone.
            
            results.append(("Error", f"{num1_str} vs {num2_str}", _error_message))
        else:
            status = "Equal" if result else "Not Equal"
            results.append((status, f"{num1_str} vs {num2_str}", None))

    # Output the test results to console (allowed as it's not an interactive prompt)
    for i, item in enumerate(results):
        print(f"\nTest Case {i+1}:")
        if item[0] == "Error":
            print(item[2])
        else:
            print(f"Values '{item[1][5:-3]}...' and '{item[1][-4:]}...': {item[0]}")

    # Final summary based on the sample block execution.
    if results[-1][0] == "Error":
        print("\nNote: The last test case involved non-integer inputs.")