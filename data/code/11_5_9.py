import math

def find_ratio_of_lengths(l1: int, l2: int) -> tuple[int, int]:
    """
    Calculates the simplified integer ratio l1 : l2 using the Euclidean algorithm 
    to compute the greatest common divisor (GCD).
    
    Args:
        l1 (int): The first length value.
        l2 (int): The second length value.
        
    Returns:
        tuple[int, int]: A tuple containing two integers representing the simplified ratio [a, b].
        
    Raises:
        ValueError: If either input is not a positive integer.
    """
    
    if not isinstance(l1, int) or not isinstance(l2, int):
        raise TypeError("Both inputs must be integers.")
    if l1 <= 0 or l2 <= 0:
        raise ValueError("Inputs must be positive integers.")

    # The Euclidean algorithm for GCD is already implemented in the standard library as math.gcd.
    gcd = math.gcd(l1, l2)
    
    numerator = l1 // gcd
    denominator = l2 // gcd
    
    return (numerator, denominator)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input.
    val_a = 40
    val_b = 56

    result_ratio = find_ratio_of_lengths(val_a, val_b)
    
    print(f"Ratio of {val_a} : {val_b} is {result_ratio[0]} : {result_ratio[1]}")