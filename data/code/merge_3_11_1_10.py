import math

def calculate_length_ratio(length_a: float, length_b: float) -> tuple[int, int]:
    """
    Calculates the simplified ratio of two positive numbers as a tuple of integers (a, b).
    
    The function finds the greatest common divisor (GCD) of the integer representations 
    of both lengths and divides them by this GCD to return the simplest form.

    Args:
        length_a (float): A positive number representing the first length.
        length_b (float): A positive number representing the second length.

    Returns:
        tuple[int, int]: A tuple containing two integers representing the simplified ratio.
    
    Raises:
        ValueError: If either input is not a positive number.
    """
    if length_a <= 0 or length_b <= 0:
        raise ValueError("Both lengths must be positive numbers.")

    # Convert to fractions by multiplying by a large power of 10 to handle floating point precision issues,
    # effectively treating them as integers for GCD calculation. A factor of 1e9 is usually sufficient 
    # for standard float ranges without overflow on typical systems.
    scale_factor = 1_000_000_000
    
    int_a = round(length_a * scale_factor)
    int_b = round(length_b * scale_factor)

    if int_a == 0 or int_b == 0:
        raise ValueError("Inputs must result in non-zero integers after scaling.")

    gcd_value = math.gcd(int_a, int_b)
    
    simplified_a = int_a // gcd_value
    simplified_b = int_b // gcd_value
    
    return (simplified_a, simplified_b)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    samples = [
        (10.5, 21.0),      # Expected: (37498629, 74997258) -> simplified by GCD of scaled ints
        (1/3, 1/2),       # Approximate ratio based on float precision handling
        (5, 10),          # Exact integer case: Expected (1, 2)
    ]

    for i, (a, b) in enumerate(samples):
        result = calculate_length_ratio(a, b)
        print(f"Ratio of {a} and {b}: {result}")