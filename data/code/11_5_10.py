import math

def find_ratio_of_lengths(l1: int, l2: int) -> tuple[int, int]:
    """
    Calculates the simplified integer ratio of two lengths (l1 : l2).
    
    Uses the Euclidean algorithm via Python's built-in GCD to simplify the fraction.
    
    Args:
        l1 (int): The first length value.
        l2 (int): The second length value.
        
    Returns:
        tuple[int, int]: A tuple containing the simplified numerator and denominator.
                         If inputs are negative, signs are preserved in the ratio logic 
                         by dividing both by GCD which handles magnitude reduction;
                         however, standard mathematical simplification assumes non-negative integers.
                         Assuming input constraints of positive integers based on 'length' semantics.
    
    Raises:
        ValueError: If either length is zero or negative.
    """
    if l1 <= 0 or l2 <= 0:
        raise ValueError("Lengths must be positive integers.")

    # Calculate the Greatest Common Divisor (GCD) using Euclidean algorithm logic via math.gcd
    common_divisor = math.gcd(l1, l2)

    simplified_l1 = l1 // common_divisor
    simplified_l2 = l2 // common_divisor

    return simplified_l1, simplified_l2

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies.
    sample_inputs = [
        (40, 60),   # Expected output: (2, 3)
        (8, 10),    # Expected output: (4, 5)
        (9, 12),    # Expected output: (3, 4)
        (7, 5),     # Expected output: (7, 5) - already coprime
    ]

    print("Testing find_ratio_of_lengths function:")
    for l1_val, l2_val in sample_inputs:
        ratio = find_ratio_of_lengths(l1_val, l2_val)
        print(f"Ratio of {l1_val} : {l2_val} is simplified to {ratio[0]} : {ratio[1]}")