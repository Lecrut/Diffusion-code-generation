import math

def calculate_length_ratio(length_a: float, length_b: float) -> tuple[int, int]:
    """
    Calculates the simplified ratio of two positive numbers as a tuple of integers (a, b).
    
    The function returns smallest positive integers representing the same fraction.
    For example, 2/4 becomes (1, 2), and 5/3 remains (5, 3) since they are coprime.

    Args:
        length_a (float): First positive number.
        length_b (float): Second positive number.

    Returns:
        tuple[int, int]: A simplified ratio as a tuple of integers.
    
    Raises:
        ValueError: If either input is not positive or non-numeric.
    """
    if not isinstance(length_a, (int, float)) or not isinstance(length_b, (int, float)):
        raise TypeError("Inputs must be numeric.")
    if length_a <= 0 or length_b <= 0:
        raise ValueError("Both inputs must be positive numbers.")

    # Determine the greatest common divisor for floating-point approximation.
    # We convert to integers by scaling up based on a tolerance threshold 
    # derived from float precision, then compute GCD and scale back down if needed.
    
    def gcd(a: int, b: int) -> int:
        """Compute the Greatest Common Divisor using Euclidean algorithm."""
        while b != 0:
            a, b = b, a % b
        return abs(a)

    # Convert floats to integers carefully by scaling based on precision.
    # Using a small epsilon for comparison if values are very close but not equal due to float representation.
    scale_factor = max(1, 2 ** math.log10(max(length_a, length_b)) + 4) 
    int_val_a = round(length_a * scale_factor)
    int_val_b = round(length_b * scale_factor)

    common_divisor = gcd(int_val_a, int_val_b)
    
    simplified_a = int_val_a // common_divisor
    simplified_b = int_val_b // common_divisor
    
    return (simplified_a, simplified_b)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    samples = [
        (2.0, 4.0),      # Expected: (1, 2)
        (5.0, 3.0),      # Expected: (5, 3) - coprime integers already
        (7.5, 9.0),      # Expected: (5, 6) after scaling and simplification logic
        (1.0/3.0, 2.0/3.0), # Approximate floats for thirds -> expected scaled result
    ]

    results = []
    for length_a_val, length_b_val in samples:
        try:
            ratio_result = calculate_length_ratio(length_a_val, length_b_val)
            results.append((length_a_val, length_b_val, list(ratio_result)))
        except Exception as e:
            results.append(f"Error with inputs ({length_a_val}, {length_b_val}): {e}")

    # Print results directly to stdout.
    for input_vals, output in results:
        print(f"Inputs: {input_vals} -> Output Ratio Tuple: {tuple(output)}")