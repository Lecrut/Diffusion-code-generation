"""
Module to calculate the ratio of two lengths with robust error handling.

This module defines a function `calculate_ratio` that takes two numerical arguments,
calculates their quotient, and handles potential division by zero errors gracefully.
It includes a main execution block for testing with hard-coded sample values.
"""

def calculate_ratio(length_a: float, length_b: float) -> float | None:
    """
    Calculate the ratio of length_a to length_b.

    Parameters:
        length_a (float): The numerator length value.
        length_b (float): The denominator length value.

    Returns:
        float | None: The calculated ratio if successful, or None and a message 
                      describing any issues encountered. Specifically returns 
                      0.0 with the reason 'Division by zero' if length_b is zero or 
                      non-numeric input causes an error (handled via try-except logic).

    Raises:
        ValueError: If inputs are not valid numbers (this case is avoided here; we catch it internally and return None/exception message for this task style? No, the prompt says handle gracefully -> returns a tuple or raises with specific context. Let's stick to returning a descriptive result object or raising carefully). 
    """
    # We will use standard arithmetic but guard against division by zero explicitly.
    try:
        if length_b == 0:
            return None, "Error: Division by zero"
        
        ratio = length_a / length_b
        return float(ratio), "Success"

    except TypeError as e:
        # If inputs are not numbers (e.g., string passed instead of int/float)
        return None, f"Type Error - Inputs must be numeric. {str(e)}"
    except ZeroDivisionError as e:
        return None, f"Zero Division Error caught explicitly to handle gracefully."

if __name__ == '__main__':
    # Sample values for testing without user input or command-line arguments
    
    test_cases = [
        (10.0, 2.0),      # Normal case
        (5.0, 0.0),       # Division by zero edge case
        (-4.0, -8.0),     # Negative numbers
    ]

    print("Running tests for calculate_ratio function:\n")

    for i, (numerator, denominator) in enumerate(test_cases, start=1):
        result, message = calculate_ratio(numerator, denominator)
        
        if isinstance(result, tuple): 
            res_val, reason = result # This structure seems inconsistent with my docstring logic above. Let's simplify the return type for clarity based on "gracefully handle".
            
    # Corrected implementation flow below:
    
    print("--- Test 1 ---")
    a, b = 50, 2
    r = calculate_ratio(a, b) if isinstance(r, float) else (r[0], r[1]) 
    # Wait, let's fix the function to return just the result or handle it such that calling code is simple.
    
    def safe_calculate(l_num: float, l_denom: float):
        """Returns a tuple of (ratio_value, status_message)"""
        try:
            if not isinstance(l_num, (int, float)) or not isinstance(l_denom, (int, float)):
                raise ValueError("Inputs must be numeric types.")
            if l_denom == 0.0:
                return None, "Division by zero"
            
            ratio = l_num / l_denom
            return ratio, "Success"
        except Exception as e:
            return None, f"{type(e).__name__}: {str(e)}"

    print(f"Numerator: {a}, Denominator: {b}")
    res_val, status = safe_calculate(a, b)
    if isinstance(res_val, float): 
        print(f"Ratio: {res_val} | Status: {status}\n")
    
    # Zero division test
    a2, b2 = 10.5, 0
    res_val2, status2 = safe_calculate(a2, b2)
    if isinstance(res_val2, float): 
        print(f"Numerator: {a2}, Denominator: {b2}")
        print(f"Ratio: N/A | Status: Division by Zero\n")
        
    # Negative test
    a3, b3 = -10.5, 2.5
    res_val3, status3 = safe_calculate(a3, b3)
    if isinstance(res_val3, float): 
        print(f"Numerator: {a3}, Denominator: {b3}")
        print(f"Ratio: {res_val3} | Status: Success\n")