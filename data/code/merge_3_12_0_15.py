import math

def simplify_ratio(ratio):
    """
    Simplifies a ratio (tuple or list of two numbers) to its lowest terms.
    
    Args:
        ratio (tuple | list): A pair of integers representing the weight ratio.
        
    Returns:
        tuple: A simplified tuple containing the reduced numerator and denominator.
            
    Raises:
        ValueError: If either number in the ratio is zero or if input types are invalid.
    """
    
    # Convert to a consistent list for processing, then back to tuple for return
    num_list = [int(x) for x in ratio]
    numerator = num_list[0]
    denominator = num_list[1]

    # Validate inputs: neither can be zero as it implies an undefined or invalid weight state.
    if numerator == 0 or denominator == 0:
        raise ValueError("Ratio components cannot be zero.")

    # Ensure positive values for standard ratio representation (e.g., -2:-4 becomes 1:2)
    sign = 1
    if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
        sign = -1
    
    numerator, denominator = abs(numerator), abs(denominator)

    # Calculate the greatest common divisor to simplify the fraction.
    gcd_value = math.gcd(int(numerator), int(denominator))

    simplified_numerator = (numerator // gcd_value) * sign
    simplified_denominator = (denominator // gcd_value) * sign

    return tuple([simplified_numerator, simplified_denominator])

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input.
    
    # Sample 1: Standard positive integers
    ratio_1 = [40, 60]
    result_1 = simplify_ratio(ratio_1)
    print(f"Input {ratio_1} -> Simplified Ratio: {result_1}")

    # Sample 2: Negative numbers (should preserve sign logic or normalize to positive based on context; here normalized with sign handling)
    ratio_2 = [-3, -9]
    result_2 = simplify_ratio(ratio_2)
    print(f"Input {ratio_2} -> Simplified Ratio: {result_2}")

    # Sample 3: Mixed signs (should normalize to positive denominator or consistent sign convention; here normalized with sign handling)
    ratio_3 = [10, -5]
    result_3 = simplify_ratio(ratio_3)
    print(f"Input {ratio_3} -> Simplified Ratio: {result_3}")

    # Sample 4: Using tuple input format as requested in task description.
    ratio_4 = (2, 8)
    result_4 = simplify_ratio(ratio_4)
    print(f"Input {ratio_4} -> Simplified Ratio: {result_4}")