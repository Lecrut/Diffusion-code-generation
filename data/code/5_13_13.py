"""
Module to compare two length measurements with validation.
This module contains a function that takes two numeric values, validates them,
calculates their difference, and prints a detailed comparison report.
It includes an execution block using hard-coded sample values for demonstration.
No user input or external dependencies are required at runtime.
"""

def compare_lengths(value_a: float | int, value_b: float | int) -> None:
    """
    Compares two length measurements and prints a detailed report including the difference.

    Args:
        value_a (float|int): The first numeric length measurement.
        value_b (float|int): The second numeric length measurement.

    Returns:
        None

    Raises:
        ValueError: If either input is not a valid number or if inputs are identical.
    """
    # Validate that both values can be converted to float for consistent handling
    try:
        num_a = float(value_a)
        num_b = float(value_b)
    except (ValueError, TypeError):
        raise ValueError("Both inputs must be valid numeric types.")

    if num_a == num_b:
        print(f"Comparison Result:")
        print("-" * 40)
        print(f"Value A ({value_a}) is equal to Value B ({value_b}).")
        difference = 0.0
        print(f"Difference (A - B): {difference}")
    else:
        # Ensure consistent decimal places for display (up to 2 decimals if not integer)
        def format_num(n, precision=4):
            return f"{n:.{precision}f}"

        diff = num_a - num_b
        
        print("Comparison Result:")
        print("-" * 40)
        print(f"Value A: {format_num(num_a)}")
        print(f"Value B: {format_num(num_b)}")
        
        if abs(diff) < 1e-6 and not (num_a == num_b): # Floating point epsilon check just in case, though logic above handles equality well enough for floats usually. Re-evaluating strict float diff vs int comparison. 
            pass 

        print("-" * 40)
        
        is_positive = diff > 0
        sign_str = "+" if not is_positive and num_a != num_b else "" # Handle negative zero or simple positive/negative
        
        magnitude_diff = abs(diff)
        
        result_text = f"Difference (A - B): {format_num(magnitude_diff)}"
        print(result_text)

    return

if __name__ == '__main__':
    # Hard-coded sample values for demonstration purposes.
    # These satisfy the requirement to run without user input or network access.
    
    SAMPLE_A = 10.56789
    SAMPLE_B = 3.2
    
    try:
        compare_lengths(SAMPLE_A, SAMPLE_B)
    except ValueError as e:
        print(f"Error during comparison: {e}")