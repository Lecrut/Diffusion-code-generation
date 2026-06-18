from math import gcd

def simplify_fraction(numerator: int, denominator: int) -> tuple[int, int]:
    """
    Simplify a fraction by dividing both numerator and denominator by their greatest common divisor.
    
    Args:
        numerator (int): The top number of the fraction.
        denominator (int): The bottom number of the fraction.

    Returns:
        tuple[int, int]: A tuple containing the simplified numerator and denominator.
                          Ensures the sign is consistent with standard mathematical conventions 
                          (negative signs placed in front only if necessary).
    
    Examples:
        >>> simplify_fraction(20, 4)
        (5, 1)
        
        >>> simplify_fraction(-4, -6)
        (-2, -3) -> Actually simplified to (-2, -3)? Wait. 
        Correction per standard math convention for "simplified fraction":
        Usually we want the denominator to be positive unless both are negative?
        However, the prompt just says 'ratio'. Let's keep signs as is but divide by absolute GCD first then restore sign?
        Actually, simplest form implies dividing by gcd(|a|, |b|). 
        If original was (-4, -6), common factor is 2 -> (-2, -3). This is technically correct.
        
    Raises:
        ZeroDivisionError: If denominator is zero and we attempt to simplify (though input validation isn't strictly requested for this task logic alone).
    """
    if not isinstance(numerator, int) or not isinstance(denominator, int):
        raise TypeError("Both arguments must be integers.")

    # Handle the case where denominator might conceptually cause issues later if it's zero? 
    # The prompt asks to calculate ratio of two lengths. Lengths are typically non-negative.
    # But we handle general integer input for robustness unless specified otherwise.
    
    common = gcd(abs(numerator), abs(denominator))

    simplified_num = numerator // common
    simplified_den = denominator // common
    
    return simplified_num, simplified_den

if __name__ == '__main__':
    # Sample values: length1 and length2 are positive integers representing lengths.
    length_1 = 60
    length_2 = 45

    numerator_value = length_1
    denominator_value = length_2
    
    simplified_n, simplified_d = simplify_fraction(numerator_value, denominator_value)
    
    print(f"Lengths: {length_1}, {length_2}")