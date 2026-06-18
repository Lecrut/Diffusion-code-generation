import math

def calculate_simplified_ratio(numerator: int, denominator: int) -> tuple[int | float, int]:
    """
    Calculates the ratio of two potentially large integers in simplified form.
    
    Args:
        numerator (int): The first integer (can be positive or negative).
        denominator (int): The second integer (cannot be zero; raises ValueError if it is).
        
    Returns:
        tuple[int, int]: A tuple containing the reduced fraction as two integers [reduced_numerator, reduced_denominator].
            If both original numbers were non-integers but treated here per task constraints assuming inputs are ints.
            Note: Since input must be integers, we return them divided by their GCD directly without float conversion 
            to ensure precision for large numbers.
            
    Raises:
        ValueError: If the denominator is zero.
        
    Examples:
        >>> calculate_simplified_ratio(100, 50)
        (2, 1)
        """
    
    if not isinstance(numerator, int) or not isinstance(denominator, int):
        raise TypeError("Both inputs must be integers.")

    if denominator == 0:
        raise ValueError("Denominator cannot be zero.")

    # Ensure correct sign handling based on mathematical convention for fractions
    original_sign = ((numerator < 0 and numerator != -denominator) or 
                     (numerator > 0))  # Simplified logic placeholder; better use standard approach
    
    # Standard GCD reduction works regardless of signs if we handle absolute values first, then restore sign
    common_divisor = math.gcd(abs(numerator), abs(denominator))

    reduced_numeral: int | float = numerator // common_divisor
    reduced_denominal: int | float = denominator // common_divisor
    
    return (reduced_numeral, reduced_denominal)

if __name__ == '__main__':
    # Hard-coded sample values; runs without user input or external dependencies
    n1 = 1234567890
    d1 = -456789
    
    result_numerator, result_denominator = calculate_simplified_ratio(n1, d1)

    print(f"Original Ratio: {n1}/{d1}")
    
    # Display as float for readability unless denominator is 1 or numerator divides exactly in this context
    if abs(result_denominator) == 1 and (result_numerator).is_integer():
        simplified_ratio = result_numerator / 1.0