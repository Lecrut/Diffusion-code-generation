import sys

def simplify_ratio(a: int, b: int) -> str:
    """Return a fully simplified ratio string 'a:b'."""
    if not (isinstance(a, int) and isinstance(b, int)):
        raise ValueError("Both inputs must be integers.")
    
    common = gcd(abs(a), abs(b))
    return f"{(a // common)}:{(b // common)}"

def gcd(x: int, y: int) -> int:
    """Compute the greatest common divisor using Euclidean algorithm."""
    while y != 0:
        x, y = y, x % y
    return abs(x)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed.
    ratio_a = 48
    ratio_b = 18
    
    try:
        result = simplify_ratio(ratio_a, ratio_b)
        print(result)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)