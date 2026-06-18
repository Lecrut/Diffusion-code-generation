import math

def find_ratio_of_lengths(l1: int, l2: int) -> tuple[int, int]:
    """
    Calculates the simplified ratio of two integers l1 : l2.
    
    Uses the Euclidean algorithm via math.gcd to simplify the fraction.
    
    Args:
        l1 (int): The first length value.
        l2 (int): The second length value.
        
    Returns:
        tuple[int, int]: A simplified ratio represented as a tuple (a, b) 
                         such that a/b = l1/l2 and gcd(a, b) == 1.
    
    Raises:
        ValueError: If either input is zero or negative.
    """
    if l1 <= 0 or l2 <= 0:
        raise ValueError("Lengths must be positive integers.")

    common_divisor = math.gcd(l1, l2)
    simplified_l1 = l1 // common_divisor
    simplified_l2 = l2 // common_divisor
    
    return (simplified_l1, simplified_l2)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    sample_lengths_1 = 8
    sample_lengths_2 = 4

    result_ratio = find_ratio_of_lengths(sample_lengths_1, sample_lengths_2)
    
    print(f"Ratio of {sample_lengths_1} : {sample_lengths_2}")
    print(f"Simplified: {result_ratio[0]} : {result_ratio[1]}")