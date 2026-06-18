import math

def simplify_ratio(ratio1: float, ratio2: float) -> tuple[int, int]:
    """
    Simplifies two weight ratios into a coprime integer pair (a, b).
    
    The function converts the input floats to integers by scaling them up 
    if necessary to avoid floating-point inaccuracies during GCD computation.
    It then divides both numbers by their greatest common divisor (GCD)
    and returns the simplified tuple as positive integers.

    Args:
        ratio1 (float): First weight ratio value.
        ratio2 (float): Second weight ratio value.

    Returns:
        tuple[int, int]: A tuple containing two coprime integers representing 
                         the simplified ratio of input values.
    
    Raises:
        ValueError: If both inputs are zero or if one is non-zero and the other is effectively zero.
    """
    # Handle edge cases where either value might be too small to represent meaningfully as an integer directly,
    # by scaling them up based on a reasonable precision factor (e.g., 10^6) before conversion.
    scale_factor = 1_000_000
    
    int_ratio1 = round(ratio1 * scale_factor)
    int_ratio2 = round(ratio2 * scale_factor)

    # Ensure non-negative values for GCD calculation and logical consistency in ratios
    if int_ratio1 < 0:
        int_ratio1, int_ratio2 = -int_ratio1, -int_ratio2
    elif int_ratio2 < 0:
        raise ValueError("Ratios must be non-negative.")

    # Handle the case where both are zero (undefined ratio) or one is effectively zero relative to the other.
    if int_ratio1 == 0 and int_ratio2 == 0:
        raise ValueError("Cannot simplify a zero-to-zero ratio; inputs should not be simultaneously zero.")
    
    if int_ratio1 == 0:
        return (int_ratio2, 1)
    elif int_ratio2 == 0:
        return (int_ratio1, 1)

    # Calculate GCD of the scaled integers to simplify the ratio.
    gcd = math.gcd(int_ratio1, int_ratio2)
    
    simplified_a = int_ratio1 // gcd
    simplified_b = int_ratio2 // gcd
    
    return (simplified_a, simplified_b)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    samples = [
        ((30.5, 45.7), "Example with floating point inputs"),
        ((1/2, 1/3), "Simple fractions converted to decimals internally"),
        ((100, 200), "Integer ratio that simplifies easily"),
        ((-10, -20), "Negative ratios (should be handled as positive for magnitude)"),
    ]

    print("Running simplify_ratio tests...\n")
    
    for i, (inputs, description) in enumerate(samples):
        try:
            result = simplify_ratio(*inputs)
            print(f"Test {i+1}: {description}")
            print(f"  Input: ({inputs[0]}, {inputs[1]}) -> Output: {result}\n")
            
            # Verify coprimality for sanity check in the output block
            a, b = result
            if math.gcd(a, b) == 1 and a > 0 and b > 0:
                print(f"  Verification: GCD({a}, {b}) is 1. Coprime confirmed.\n")
        except ValueError as e:
            print(f"Test {i+1}: {description} -> Error: {e}\n")

    # Additional specific test case for robustness
    special_case = (0.3, 0.6)
    result_special = simplify_ratio(*special_case)
    print("Special Case Test:")
    print(f"Input: ({special_case[0]}, {special_case[1]}) -> Output: {result_special}")