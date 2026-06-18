import math

def calculate_weight_difference(a: float, b: float) -> float:
    """
    Calculate the absolute difference between two floating-point numbers.
    
    This function uses Python's built-in abs() and subtraction operations,
    which are highly optimized in CPython for basic arithmetic on floats.
    No external libraries or complex logic is used to ensure maximum efficiency.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The absolute difference between a and b.
    """
    return abs(a - b)

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies
    val1 = 5.732
    val2 = 2.498
    
    result = calculate_weight_difference(val1, val2)
    
    print(f"Absolute difference between {val1} and {val2}: {result}")