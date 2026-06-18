import sys

def is_zero(number):
    """
    Check if a given number is exactly zero.
    
    This function accepts both integer and floating-point types, but strictly checks 
    numerical equality to 0. It does not handle non-numeric inputs as the task specifies 
    checking an 'input number'. If a string or other type is passed, it will raise a TypeError.

    Args:
        number (int | float): The input value to check against zero.

    Returns:
        bool: True if number equals 0 exactly; False otherwise.
    
    Raises:
        TypeError: If the input is not an instance of int or float.
    """
    return isinstance(number, (int, float)) and number == 0

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    test_values = [0, -1, 2.5, 0.0, float('inf'), "not a number"]

    print("Testing is_zero function:")
    
    for val in test_values:
        try:
            result = is_zero(val)
            status_str = f"{val} -> {result}"
            if isinstance(result, bool):
                sys.stderr.write(f"Test passed. Result type: <class 'bool'>\n")
            else:
                # Fallback just in case logic changes unexpectedly to non-boolean return (unlikely here)
                print(status_str + " [UNEXPECTED RETURN TYPE]")
        except TypeError as e:
            sys.stderr.write(f"Test failed. {val} is not a numeric type.\n")