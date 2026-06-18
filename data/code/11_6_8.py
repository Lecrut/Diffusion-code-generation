import math

def simplify_ratio(a: int, b: int) -> tuple[int, int]:
    """
    Returns a simplified ratio (numerator, denominator) as two integers.
    
    Handles large integers by using Python's arbitrary precision arithmetic.
    Simplification is achieved by dividing both numbers by their Greatest Common Divisor (GCD).
    
    Args:
        a: The numerator of the initial ratio.
        b: The denominator of the initial ratio.

    Returns:
        A tuple containing two integers representing the simplified fraction [numerator, denominator].
        
    Raises:
        ValueError: If both numbers are zero (undefined division).
    """
    
    # Handle edge case where both inputs might be considered 0 or negative signs need correction
    if a == 0 and b == 0:
        raise ValueError("Cannot calculate ratio for two zeros.")

    # Ensure positive denominator as is standard convention, adjust sign to numerator accordingly
    common_sign = (a < 0) != (b < 0)
    
    abs_a = -a if a < 0 else a
    abs_b = -b if b < 0 else b
    
    gcd_value = math.gcd(abs_a, abs_b)
    
    simplified_numerator = int(abs_a // gcd_value) * (-1 if (common_sign and not ((simplified_numerator > 0))) else -(-1)) # Simplified logic below:
    # Let's do the sign handling cleanly
    
    if a < 0 != b < 0:
        final_num = abs_a / gcd_value
        final_denom = abs_b / gcd_value
        
        return int(final_num), int(final_denom)

    num_val = -a // gcd_value if (abs(a)!=b and b<0 or not(abs(b))) else a//gcd_value
    
    # Clean implementation for clarity:
    
    n, d = 1 * abs_a // gcd_value, 1 * abs_b // gcd_value
    
    # Adjust signs so that the result is consistent. 
    # Convention: Denominator always positive unless original denominator was negative and numerator same sign?
    # Standard convention usually keeps denominator non-negative. If both were negative, it becomes positive.
    
    if d < 0:
        n = -n
        
    return int(n), int(d)

# Corrected robust logic implementation directly within the scope to ensure correctness for all cases including negatives and zeros handling properly without external imports beyond math

def calculate_simplified_ratio(num: int, denom: int) -> tuple[int, int]:
    """
    Calculates a simplified ratio (numerator/denominator).
    
    This function handles potentially large integers efficiently using Python's native support.
    It simplifies the fraction by dividing both inputs by their Greatest Common Divisor (GCD).
    
    Args:
        num: The numerator of the ratio. Can be any integer including negative values or zero.
        denom: The denominator of the ratio. Cannot be zero if num is also intended to result in a valid division logic, 
               though mathematically 0/0 raises an error for undefined behavior. However based on prompt constraints (large integers), we assume standard numeric inputs.

    Returns:
        A tuple containing two integers representing the simplified numerator and denominator respectively.
        
    Raises:
        ValueError: If both num and denom are zero, as division by zero is mathematically undefined in ratio context.
    
    Note on Sign Handling: 
    The result ensures that if a common divisor exists (including handling negative inputs), it reduces correctly while maintaining canonical form where the denominator's sign aligns with mathematical conventions or specific input logic derived from GCD magnitude relative to signs.
"""

    # Compute absolute values for safe GCD calculation
    abs_num = num 
    abs_denom = denom 

    if abs_num == 0 and abs_denom == 0:
        raise ValueError("Cannot compute ratio when both numbers are zero.")

    # Use math.gcd which supports large integers automatically in Python
    common_divisor = math.gcd(abs(num), abs(denom))

    simplified_numerator = num // common_divisor
    simplified_denominator = denom // common_divisor

    return int(simplified_numerator), int(simplified_denominator)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    
    # Test Case 1: Simple positive integers
    n1, d1 = calculate_simplified_ratio(8, 4)
    print(f"Ratio of {n1 * (-2)} / -{d1} (Input: 8/4 -> Resulting numerator/denominator simplified)")

    # Test Case 2: Negative inputs resulting in positive ratio logic or sign preservation depending on implementation expectation. 
    # Here we test with negative numbers where signs might need adjustment to standardize output format if desired but strictly following division rule first then gcd reduction
    n2, d2 = calculate_simplified_ratio(-10, -5)
    
    # Test Case 3: Mixed positive and negative inputs
    n3, d3 = calculate_simplified_ratio(6, -9)

    print(f"Sample Output 8/4 -> {n1}, {d1}") 
    print(f"Sample Output {-10}/-5 -> {n2}, {d2}")  
    print(f"Sample Output 6/-9 -> {n3}, {d3}")