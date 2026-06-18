import math

def calculate_length_ratio(length_a: float, length_b: float) -> tuple[int, int]:
    """
    Returns the simplified ratio of two positive numbers as a tuple of integers (numerator, denominator).
    
    Args:
        length_a: A positive number representing the first value.
        length_b: A positive number representing the second value.
        
    Returns:
        A tuple containing two integers that represent the simplified ratio of length_a to length_b.
    """
    if length_a <= 0 or length_b <= 0:
        raise ValueError("Both input lengths must be positive numbers.")

    # Convert to integers first, assuming inputs are meant to be treated as comparable units directly
    int_a = int(round(length_a))
    int_b = int(round(length_b))
    
    if int_a == 0 or int_b == 0:
        raise ValueError("Neither input length can be zero after rounding.")

    # Calculate the greatest common divisor (GCD) of the two integers
    gcd_value = math.gcd(int_a, int_b)

    # Divide both numbers by their GCD to get the simplified ratio
    numerator = int_a // gcd_value
    denominator = int_b // gcd_value
    
    return (numerator, denominator)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_1_a = 3.0
    sample_1_b = 5.0
    result_1 = calculate_length_ratio(sample_1_a, sample_1_b)

    sample_2_a = 8.4
    sample_2_b = 6.0
    # Note: Inputs are treated as integers here (rounded), so 8 and 6 -> gcd(8,6)=2 -> 4/3
    result_2 = calculate_length_ratio(sample_2_a, sample_2_b)

    print(f"Ratio of {sample_1_a} to {sample_1_b}: {result_1}")
    print(f"Ratio of {sample_2_a} to {sample_2_b}: {result_2}")