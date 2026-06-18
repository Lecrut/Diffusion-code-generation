import math

def is_close(a: float, b: float) -> bool:
    """
    Check if two floating-point numbers are close in value within a specified tolerance.
    
    This function uses relative and absolute tolerances to determine equality,
    which is robust against rounding errors that occur during arithmetic operations.
    
    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.
        
    Returns:
        bool: True if the numbers are close within tolerance, False otherwise.
    """
    # Default tolerances based on common practices for floating-point comparison
    rtol=1e-9  # Relative tolerance
    atol=1e-12  # Absolute tolerance
    
    return abs(a - b) <= (rtol * max(abs(a), abs(b)) + atol)

if __name__ == '__main__':
    # Sample test cases to demonstrate the function without user input or external dependencies
    
    # Test case 1: Two identical integers represented as floats
    num_a = 3.0
    num_b = float(3)
    
    # Test case 2: Floating-point arithmetic result vs expected value (common rounding error scenario)
    calc_result = math.sqrt(4) + 1e-9
    exact_value = 3
    
    # Test case 3: Clearly different numbers
    diff_a = 0.5
    diff_b = 0.6
    
    print(f"Test Case 1 (Identical floats): {num_a} vs {num_b}")
    if is_close(num_a, num_b):
        print("Result: Equal")
    else:
        print("Result: Not equal")

    print("\nTest Case 2 (Arithmetic with potential rounding error)")
    print(f"Calculated value: {calc_result}, Expected exact value: {exact_value}")
    if is_close(calc_result, exact_value):
        print("Result: Close enough within tolerance")
    else:
        print("Result: Not close")

    print("\nTest Case 3 (Clearly different values)")
    print(f"Value A: {diff_a}, Value B: {diff_b}")
    if is_close(diff_a, diff_b):
        print("Result: Equal")
    else:
        print("Result: Not equal")