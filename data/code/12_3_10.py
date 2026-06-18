import sys

def simplify_ratio(numerator: int, denominator: int) -> tuple[int, int]:
    """Simplify a fraction by dividing both parts by their greatest common divisor."""
    if numerator == 0 and denominator == 0:
        raise ValueError("Cannot determine ratio for zero/zero.")

    # Handle negative numbers to ensure the result has positive denominator
    sign = -1 if (numerator < 0) != (denominator < 0) else 1
    num, den = abs(numerator), int(abs(denominator))

    gcd_val = _gcd(num, den)
    
    simplified_num = numerator // gcd_val * sign
    simplified_den = denominator // gcd_val
    
    return simplified_num, simplified_den

def _gcd(a: int, b: int) -> int:
    """Calculate the greatest common divisor using Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a

class RatioError(Exception):
    """Custom exception for invalid ratio inputs."""
    pass

def get_integer_input(prompt_msg: str) -> int | None:
    """Simulates getting an integer input without using sys.stdin or argparse.
    
    Since the task forbids interactive prompts and requires no user input,
    this function is designed to be called only within a context where 
    valid integers are expected (e.g., from pre-calculated data).
    
    However, per instructions: 'Never call input(), sys.stdin...'.
    The actual execution logic will rely on the hardcoded sample block.
    """
    # This function is kept for potential future use or if called programmatically 
    # with a mock object in tests, but main relies solely on pre-defined values.
    return None

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input
    ratio_a = 120
    ratio_b = 45

    try:
        simplified_num, simplified_den = simplify_ratio(ratio_a, ratio_b)
        
        print(f"Input Ratio ({ratio_a}:{ratio_b})")
        print(f"Simplified Result: {simplified_num}/{simplified_den}")
    
    except ValueError as ve:
        print(f"Error: Invalid input detected - {ve}", file=sys.stderr)
        sys.exit(1)