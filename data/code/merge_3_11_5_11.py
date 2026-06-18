import math

def find_ratio_of_lengths(l1: int, l2: int) -> tuple[int, int]:
    """
    Calculates the simplified integer ratio of two lengths (l1 : l2).
    
    Args:
        l1 (int): The first length.
        l2 (int): The second length.
        
    Returns:
        tuple[int, int]: A tuple containing the numerator and denominator 
                         of the simplified ratio. Assumes inputs are non-negative integers.
                         
    Raises:
        ValueError: If either input is negative or zero (to avoid division by zero).
    """
    if l1 < 0 or l2 < 0:
        raise ValueError("Lengths must be non-negative.")
    
    # Handle the case where both are zero; undefined ratio, return zeros.
    if l1 == 0 and l2 == 0:
        return (0, 0)

    # Calculate GCD using math.gcd which implements Euclidean algorithm efficiently in Python
    common_divisor = math.gcd(l1, l2)
    
    numerator = l1 // common_divisor
    denominator = l2 // common_divisor
    
    return (numerator, denominator)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    sample_lengths_1 = 80
    sample_lengths_2 = 45

    result_ratio = find_ratio_of_lengths(sample_lengths_1, sample_lengths_2)
    
    print(f"Ratio of {sample_lengths_1} : {sample_lengths_2}")
    print(f"Simplified Ratio: {result_ratio[0]} : {result_ratio[1]}")