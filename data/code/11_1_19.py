import math

def calculate_length_ratio(length_a: float, length_b: float) -> tuple[int, int]:
    """
    Calculates the simplified ratio of two positive numbers as a tuple of integers (a, b).
    
    Args:
        length_a (float): The first positive number.
        length_b (float): The second positive number.
        
    Returns:
        tuple[int, int]: A tuple containing the numerator and denominator of the simplified ratio.
    """
    if length_a <= 0 or length_b <= 0:
        raise ValueError("Both lengths must be positive numbers.")

    # Convert to integers by rounding after scaling to avoid floating point precision issues with very small/large numbers,
    # but since inputs are floats representing ratios directly, we can work with the float values.
    # To get integer ratio a/b = length_a/length_b => a : b where gcd(a,b)=1
    
    # We need to find integers A and B such that A/B approximates length_a/length_b exactly if possible within reason,
    # but typically for "simplified ratio" of floats, we treat them as exact values scaled up.
    # However, the most robust interpretation without arbitrary precision libraries is:
    # Find GCD of (round(length_a * scale), round(length_b * scale)) for a large enough scale? 
    # Actually, standard approach for float ratios to integers often implies treating them as if they were exact fractions.
    # But since floats are inexact representations, the most logical "simplified ratio" is:
    # Let's assume the inputs represent values that can be represented exactly by scaling up to a common denominator or simply 
    # using the GCD of their integer parts if they happen to be integers? No.
    
    # Re-evaluating based on typical coding interview context for "ratio":
    # If length_a = 1.5 and length_b = 2.0, ratio is 3:4.
    # We can multiply both by a large power of 10 to convert to integers, then find GCD.
    
    scale_factor = 10 ** 6  # Sufficient for most decimal inputs up to 6 decimal places
    
    int_a = round(length_a * scale_factor)
    int_b = round(length_b * scale_factor)

    if int_a == 0 or int_b == 0:
        raise ValueError("Lengths must be positive.")

    common_divisor = math.gcd(int_a, int_b)
    
    return (int_a // common_divisor, int_b // common_divisor)

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input.
    samples = [
        (10, 20),       # Expected: (1, 2)
        (3, 5),         # Expected: (3, 5)
        (4.5, 6.0),     # Expected: (3, 4) -> scaled to integers first? 
                       # Let's trace: 4.5 * 1e6 = 4500000, 6.0 * 1e6 = 6000000
                       # GCD(4500000, 6000000) = 1500000 -> (3, 4). Correct.
        (2/3, 1),       # Expected: Depends on float precision of 2/3 
                       # 0.666... * 1e6 = 666667 approx? Or round(2000000/3) -> 666667
                       # GCD might not be perfect if floating point error exists.
        (5, 8),         # Expected: (5, 8)
    ]

    for i, (a, b) in enumerate(samples):
        result = calculate_length_ratio(a, b)
        print(f"Ratio of {a} and {b}: {result}")