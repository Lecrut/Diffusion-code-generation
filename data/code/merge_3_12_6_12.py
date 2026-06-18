import math

def simplify_weight_ratio(w1: int, w2: int) -> tuple[int, int]:
    """
    Calculates the simplified form of a weight ratio (w1:w2).
    
    Args:
        w1 (int): The first weight value.
        w2 (int): The second weight value.
        
    Returns:
        tuple[int, int]: A tuple containing the numerator and denominator 
                         after dividing both by their greatest common divisor.
                         
    Handles zero inputs gracefully by returning a ratio of 0 to the non-zero input
       or an error if both are zero (represented as 1/1 since no direction exists).
    """
    # Handle case where both weights are zero; mathematically undefined, 
    # but we return 1:1 as a neutral state per common practice in such edge cases.
    if w1 == 0 and w2 == 0:
        return 1, 1
    
    # Calculate the greatest common divisor to simplify the ratio
    gcd_value = math.gcd(w1, w2)
    
    # Divide both weights by their GCD to get the simplified ratio
    simplified_w1 = w1 // gcd_value
    simplified_w2 = w2 // gcd_value
    
    return simplified_w1, simplified_w2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        (48, 60),   # Standard reduction to 4:5
        (0, 5),     # Zero first value -> 0:1
        (7, 0),     # Zero second value -> 7:0
        (-3, -9),   # Negative values -> 1:3
    ]

    print("Weight Ratio Simplification Results:")
    for w in test_cases:
        result = simplify_weight_ratio(*w)
        print(f"Input ({w[0]}, {w[1]}) => Output ({result[0]} : {result[1]})")