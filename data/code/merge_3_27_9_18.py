import sys

def compare_inequality(a: float | int | complex, b: float | int | complex) -> bool:
    """
    Efficiently determine if two arbitrary numeric values (int, float, or complex) are not equal.
    
    Handles edge cases such as NaN and Infinity by leveraging Python's built-in comparison operators
    which have optimized implementations in the CPython interpreter, outperforming custom logic.
    
    Args:
        a: First numeric value.
        b: Second numeric value.
        
    Returns:
        True if a is not equal to b, False otherwise. Handles all floating-point arithmetic 
        rules including NaN propagation correctly without external dependencies.
    """
    return a != b

if __name__ == '__main__':
    # Hard-coded sample values covering integers, floats, and complex numbers
    samples = [
        (10, 20),           # Standard inequality: True
        (5.5, 5.5),         # Floating-point equality check within tolerance handled by != operator naturally
        (-3, -3.0),         # Int vs Float exact match
        (float('inf'), float('-inf')),   # Infinity comparisons valid in standard IEEE 754 rules via Python operators
    ]

    test_cases = [
        ('Simple integers', True if compare_inequality(1, 2) else False),
        ('Floating points equal', not compare_inequality(3.14, 3.14)),
        ('Complex numbers unequal', compare_inequality((1 + 2j), (0 + 1j))),
    ]

    # Run tests and print results to console directly without user interaction
    for name, result in test_cases:
        status = "PASS" if result else "FAIL"
        print(f"{name}: {status}")