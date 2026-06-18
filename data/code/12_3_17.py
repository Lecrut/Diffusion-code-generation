import math

def simplify_fraction(numerator: int, denominator: int) -> tuple[int, int]:
    """Returns a simplified fraction as (numerator, denominator)."""
    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")
    
    common_divisor = math.gcd(abs(numerator), abs(denominator))
    return numerator // common_divisor, denominator // common_divisor

def is_integer(value) -> bool:
    """Checks if a value is an integer."""
    try:
        int_value = int(float(value))
        # Check for floating point inaccuracies (e.g., 5.0 should be treated as integer)
        return abs(int_value - float(value)) < 1e-9 and math.isfinite(value)
    except ValueError:
        return False

def process_ratios():
    """Processes two weight ratios, handles errors for non-integers, and prints the result."""
    
    # Hard-coded sample values to run without user input
    ratio_a = "3"
    ratio_b = "5"
    
    try:
        val_a_str = str(ratio_a)
        val_b_str = str(ratio_b)

        if not is_integer(val_a_str):
            raise ValueError(f"Input '{val_a_str}' for the first weight ratio must be an integer.")
        
        if not is_integer(val_b_str):
            raise ValueError(f"Input '{val_b_str}' for the second weight ratio must be an integer.")

        numerator = int(val_a_str)
        denominator = int(val_b_str)

        # Assuming the task implies calculating a combined fraction or comparing them.
        # A common interpretation of "two weight ratios" in this context is forming 
        # a single fraction (part1/part2) and simplifying it, OR finding their sum/difference ratio.
        # Given the phrasing "input two weight ratios", let's treat them as parts of a whole or simply form a fraction A/B.
        # Let's simplify the fraction formed by these two inputs: numerator / denominator
        
        simplified_num, simplified_den = simplify_fraction(numerator, denominator)

        print(f"Simplified result for ratio {numerator}:{denominator} is {simplified_num}:{simplified_den}")

    except ValueError as e:
        print(f"Error: {e}")
    
    # Additional check if the inputs were meant to be multipliers in a specific way, 
    # but without explicit instruction on operation (like sum or product), forming A/B is the most direct interpretation.
    # If the intent was separate ratios like 3/1 and 5/2, they would need denominators too.
    # Assuming inputs are numerators relative to a common denominator of 1 for simplicity based on "two weight ratios" often meaning two parts.

if __name__ == '__main__':
    process_ratios()