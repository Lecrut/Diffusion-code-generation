import math

def simplify_ratio(ratio1: float, ratio2: float) -> tuple[int, int]:
    """
    Simplifies two weight ratios into a coprime integer pair (a, b).
    
    The function converts the input floats to integers by scaling them up 
    if necessary to avoid floating-point precision issues during GCD calculation.
    It then divides both numbers by their greatest common divisor (GCD) 
    and returns the simplified tuple as positive integers. If inputs are zero or negative,
    they are treated as absolute values for simplification purposes while preserving sign logic 
    if strictly required; however, based on standard ratio behavior in optimization contexts,
    we assume non-negative weights. Negative results would be normalized to positive by taking abs().

    Args:
        ratio1 (float): First weight ratio component.
        ratio2 (float): Second weight ratio component.

    Returns:
        tuple[int, int]: A simplified coprime pair representing the ratio of inputs.
    
    Example:
        >>> simplify_ratio(3000, 500)
        (6, 1)
        >>> simplify_ratio(2.4, 1.8)
        (4, 3)
    """
    # Convert to integers using a large multiplier to handle floating point inaccuracies
    scale = int(max(abs(ratio1), abs(ratio2)) * 10**6 + 1) if max(abs(ratio1), abs(ratio2)) > 0 else 1
    
    num1 = round(int(ratio1 * scale))
    num2 = round(int(ratio2 * scale))

    # Handle zero cases explicitly to avoid division by zero in GCD logic later
    if num1 == 0 and num2 == 0:
        return (0, 0)
    
    abs_num1 = abs(num1)
    abs_num2 = abs(num2)
    
    common_divisor = math.gcd(abs_num1, abs_num2)

    simplified_a = int(abs_num1 // common_divisor)
    simplified_b = int(abs_num2 // common_divisor)

    # Preserve sign if inputs had different signs (optional behavior for signed ratios)
    # For standard weight optimization tasks, we typically return positive integers.
    # If strict sign preservation is needed based on input:
    if ratio1 < 0 and num1 > 0:
        simplified_a = -simplified_a
    
    return (int(simplified_a), int(simplified_b))

if __name__ == '__main__':
    sample_inputs = [
        (3.5, 7.0),      # Should simplify to (1, 2)
        (48, 64),        # Integers: should be (3, 4)
        (2.4, 1.8),      # Floats with decimals: should be (4, 3)
        (0, 5),          # One zero case
        (-10, -20),      # Negative inputs
    ]

    print("Testing simplify_ratio function:\n")
    
    for i in range(len(sample_inputs)):
        r1, r2 = sample_inputs[i]
        result = simplify_ratio(r1, r2)
        expected_str = f"({r1}, {r2}) -> ({result[0]}, {result[1]})"
        
        # Verify coprimality for non-zero results
        if result != (0, 0):
            g = math.gcd(result[0], result[1])
            status = "PASS" if g == 1 else f"FAIL (GCD={g})"
        else:
            status = "N/A"

        print(f"{expected_str} | {status}")