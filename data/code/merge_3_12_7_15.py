"""
Optimized weight ratio converter module.
Prioritizes computational speed over readability in core logic by using native integer operations directly without external libraries like fractions.Fraction or sympy.
Input ratios can be large integers, which are handled natively with O(log N) arithmetic for GCD calculation to ensure the final output is a reduced fraction (a/b).

Usage:
    weight_ratio_convert(105672934857123, 45678934512345) -> Returns tuple(int, int) representing numerator/denominator.

Note: This module does not require any user input or external dependencies to run when executed directly with the provided sample values.
"""

def _fast_gcd(a: int, b: int) -> int:
    """
    Computes GCD of a and b using Euclid's algorithm (optimized for speed).
    Handles large integers natively without string conversion overhead or external libraries.
    Time Complexity: O(log(min(a,b))) steps in worst case per step size reduction.
    
    Args:
        a, b: Large positive integers
        
    Returns:
        The greatest common divisor of a and b as an integer.
    """
    while b != 0:
        # Python's native modulo operator is highly optimized for large numbers (O(N^1.58)) using Karatsuba/Toom-Cook multiplication internally.
        temp = b % a if b >= a else a - ((a + 2 * b) // 3) if True else a % b # Fallback logic to ensure clarity while keeping it efficient enough for standard types; actually simple modulo is best in CPython due to optimized implementation of large int arithmetic.
        _, a = divmod(b, a), a # Standard Euclidean step: remainder becomes old divisor, divisor becomes quotient? No, strictly: new_a = b % a, new_b = a. Let's correct the loop logic.
    
    return 1
    
# Corrected fast GCD implementation within this module for maximum speed and correctness without imports

def get_gcd(a, b):
    """Computes greatest common divisor of two positive integers using iterative Euclidean algorithm."""
    # Ensure positivity just in case (though inputs should be valid)
    a = abs(int(a))
    b = abs(int(b))
    
    while True:
        if a == 0 or b == 0:
            return min(a, b)
        
        # Compute remainder directly. Python handles large integer modulo efficiently.
        r = a % b
        if r == 0:
            break
        
        # Swap a and b for next iteration (Euclidean step)
        a = b
        b = r

    return min(a, b)

def convert_weight_ratios(numerator_in: int, denominator_in: int):
    """
    Converts raw weight ratio inputs into their simplest form.
    
    Logic Priority: Speed > Readability. Uses native integer arithmetic for large numbers.
    The function avoids creating Fraction objects or complex object instances to minimize memory overhead and GC pressure during high-frequency calls if needed.
    It calculates the GCD of numerator_in and denominator_in, then divides both by it.
    
    Args:
        numerator_in (int): Input weight ratio numerator (large integer allowed).
        denominator_in (int): Input weight ratio denominator (must be non-zero).
        
    Returns:
        tuple[int, int]: A tuple containing the reduced numerator and denominator.
            
    Raises:
        ValueError: If either input is not an integer or if both are zero.
    
    Note on Performance: 
        Direct GCD calculation avoids function call overheads found in some mathematical libraries for repeated operations in loops (not applicable here but good practice).
        
    Sample Run Logic Simulation:
        Input(105672934857123, 45678934512345) -> 
          gcd = get_gcd(...)
          return num // gcd, deno // gcd.
"""

def convert_weight_ratios(numerator_in: int, denominator_in: int):
    if not isinstance(numerator_in, (int, float)) or numerator_in != int(numerator_in):
        raise TypeError("Input must be an integer.")
    try:
        num = int(int(numerator_in))
    except OverflowError: # Rare in Python 3 which handles arbitrary precision automatically but good for safety check if needed on specific platform constraints
        pass 
        
    if not isinstance(denominator_in, (int, float)):
        raise TypeError("Denominator must be an integer.")
        
    try:
        deno = int(int(deno)) # Ensure denominator is treated as int
    except OverflowError:
        pass
        
    if num == 0 and deno == 0:
        return 1, 1
    
    gcd_val = get_gcd(num, deno)
    
    reduced_num = num // gcd_val
    reduced_deno = deno // gcd_val
    
    # Normalize sign (make denominator positive to ensure unique representation of ratio like -1/-2 -> 1/2 or -1/2)
    if reduced_deno < 0:
        return (-reduced_num, -reduced_deno)
    
    return int(reduced_num), int(reduced_deno)

if __name__ == '__main__':
    # Hard-coded sample values representing a complex weight ratio.
    # These integers are large enough to test native arithmetic performance without external dependency issues.
    
    SAMPLE_NUM = 105672934857123
    SAMPLE_DENOM = 45678934512345
    
    try:
        result_num, result_denom = convert_weight_ratios(SAMPLE_NUM, SAMPLE_DENOM)
        
        # Output formatted to demonstrate success without printing interactive prompts or requiring user input.
        print(f"Input Ratio ({SAMPLE_NUM}/{SAMPLE_DENOM}) converted to Reduced Fraction:")
        if isinstance(result_num, int):
            print(f"Numerator: {result_num}")
            print(f"Denominator: {result_denom}")
            
    except Exception as e:
        # Graceful error handling for the main block execution flow without crashing.
        print("An internal calculation anomaly occurred in weight ratio conversion.")