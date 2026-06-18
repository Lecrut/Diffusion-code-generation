import math

def calculate_ratio_simplified(numerator: int, denominator: int) -> tuple[int, int]:
    """
    Calculates the simplified ratio of two potentially large integers.
    
    Args:
        numerator (int): The first integer in the ratio.
        denominator (int): The second integer in the ratio.
        
    Returns:
        tuple[int, int]: A tuple containing the simplified numerator and denominator.
                         If both are zero, returns (0, 1).
    
    Raises:
        ValueError: If the denominator is zero.
    """
    if not isinstance(numerator, int) or not isinstance(denominator, int):
        raise TypeError("Both inputs must be integers.")

    # Handle edge case where both are zero
    if numerator == 0 and denominator == 0:
        return 0, 1
    
    # If the original ratio was already expressed as (a/b), we treat input 
    # as just two numbers to simplify. The prompt implies inputs like "3/4" or separate ints.
    # Assuming separate integers a and b representing 'a / b'.

    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")

    # Calculate the Greatest Common Divisor (GCD) for simplification
    gcd_value = math.gcd(numerator, denominator)

    simplified_numerator = numerator // gcd_value
    simplified_denominator = denominator // gcd_value
    
    return simplified_numerator, simplified_denominator

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input.
    num_1 = 600851475143 * 2 + 999999 
    den_1 = 12345678

    simplified_n, simplified_d = calculate_ratio_simplified(num_1, den_1)
    
    print(f"Original Ratio: {num_1} / {den_1}")
    print(f"Simplified Ratio Numerator: {simplified_n}")
    print(f"Simplified Ratio Denominator: {simplified_d}")

    # Additional test case with larger numbers and negative inputs if applicable logic holds.
    num_2 = -4800 
    den_2 = 16
    
    simplified_n2, simplified_d2 = calculate_ratio_simplified(num_2, den_2)
    
    print(f"\nSecond Test Ratio: {num_2} / {den_2}")
    print(f"Simplified Second Numerator: {simplified_n2}")
    print(f"Simplified Second Denominator: {simplified_d2}")

    # Edge case test (both zero - handled internally to return 0, 1)
    num_zero = 0 
    den_zero = 0 
    
    n_z, d_z = calculate_ratio_simplified(num_zero, den_zero)
    
    print(f"\nEdge Case Zero Ratio: {num_zero} / {den_zero}")
    print(f"Simplified Edge Numerator: {n_z}, Denominator: {d_z}")