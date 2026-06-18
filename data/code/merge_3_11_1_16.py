import math

def calculate_length_ratio(length_a: float, length_b: float) -> tuple[int, int]:
    """
    Calculates the simplified ratio of two positive numbers as a tuple of integers (a/b).
    
    Args:
        length_a: A positive number representing the first dimension.
        length_b: A positive number representing the second dimension.
        
    Returns:
        A tuple containing two integers representing the simplified ratio.
    """
    if length_a <= 0 or length_b <= 0:
        raise ValueError("Both lengths must be positive numbers.")

    # Convert to float for precision before finding GCD, then scale up to avoid floating point issues in division logic
    a = int(length_a)
    b = int(length_b)
    
    if a == 0 or b == 0:
        raise ValueError("Lengths must be positive.")

    # Find the greatest common divisor (GCD) of the two integers
    gcd_value = math.gcd(a, b)
    
    simplified_a = a // gcd_value
    simplified_b = b // gcd_value
    
    return (simplified_a, simplified_b)

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input or external dependencies
    samples = [
        (4.0, 6.0),      # Expected: (2, 3)
        (15.0, 25.0),   # Expected: (3, 5)
        (7.0, 9.0),     # Expected: (7, 9) - already coprime
        (8.0, 4.0),     # Expected: (2, 1)
    ]

    for length_a_val, length_b_val in samples:
        result = calculate_length_ratio(length_a_val, length_b_val)
        print(f"Ratio of {length_a_val} and {length_b_val}: {result}")