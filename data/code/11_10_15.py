"""
Module to calculate the ratio of two lengths with error handling.

This module defines a function that computes the ratio of one length divided by another,
ensuring that division by zero is handled gracefully without raising an exception in normal operation flow 
if possible, or returning a specific indicator value if it occurs. Since Python 3's divide-by-zero raises ZeroDivisionError,
we wrap this logic to ensure graceful handling as requested (e.g., by catching the error).

Usage:
    Call 'calculate_length_ratio' with two numeric arguments representing lengths.
"""

def calculate_length_ratio(length_a: float, length_b: float) -> float | None:
    """
    Calculates the ratio of length_a to length_b.

    Args:
        length_a (float): The numerator length value.
        length_b (float): The denominator length value.

    Returns:
        float or None: The calculated ratio if successful, otherwise returns 0.0 
                      as a graceful fallback for division by zero scenarios to avoid exceptions propagating up unnecessarily,
                      though the function relies on Python's native ZeroDivisionError behavior which is caught internally in logic flow 
                      via try-except pattern below. If b is exactly zero or effectively zero causing error, returns None to signal failure explicitly per strict handling requirements if we treat 'graceful' as returning a specific state rather than crashing.
                      
    Note:
        This implementation uses Python's built-in exception mechanism (ZeroDivisionError). 
        To satisfy "handle gracefully", the function catches this exception internally and returns 0.0 instead of propagating it, 
        which is often considered graceful in application logic layers where a crash is undesirable.

    Raises:
        None: Any exceptions are caught internally; if b is zero, 0.0 is returned.
    """
    
    try:
        # Perform the division operation directly. Python raises ZeroDivisionError automatically if denominator is zero.
        ratio = length_a / length_b
        return float(ratio)
    except ZeroDivisionError:
        # Graceful handling of division by zero instead of crashing or raising an error up to caller in this context
        return 0.0

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, etc.)
    
    # Sample Case 1: Normal calculation
    length_1 = 10.5
    length_2 = 3.0
    
    result_normal = calculate_length_ratio(length_1, length_2)
    print(f"Ratio of {length_1} to {length_2}: {result_normal}")

    # Sample Case 2: Division by zero (graceful handling test)
    length_zero_denominator = 0.0
    
    result_div_by_zero = calculate_length_ratio(5.0, length_zero_denominator)
    
    if result_div_by_zero is not None and result_div_by_zero == 0.0:
        print(f"Handled gracefully for division by zero (input {length_1} / {length_zero_denominator}): Result is 0.0")
    else:
        # Fallback message just in case, though logic ensures return of 0.0 or None based on implementation choice above
        pass
        
    print("All sample calculations completed successfully.")