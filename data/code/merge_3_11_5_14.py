def find_ratio_of_lengths(l1: int, l2: int) -> tuple[int, int]:
    """
    Calculates the simplified integer ratio l1 : l2 using the Euclidean algorithm.
    
    Args:
        l1 (int): The first length value.
        l2 (int): The second length value.
        
    Returns:
        tuple[int, int]: A tuple containing two integers representing the simplified ratio (a, b) such that a/b = l1/l2.
                       If inputs are zero or negative, it returns their absolute values in the reduced form unless they are strictly invalid cases not covered by simple reduction logic as per standard math problem context where 0:5 is usually represented as 0:1.
    
    The function assumes positive integer inputs based on the concept of 'lengths'. 
    If l2 is zero, division would be undefined; however, for ratio representation in integers like "x : y", we aim to return reduced forms.
    Standard interpretation handles non-negative integers where GCD logic applies directly or with absolute values if signs are considered (though lengths are usually positive).
    
    We use the Euclidean algorithm to find the Greatest Common Divisor (GCD) of l1 and l2, 
    then divide both by this divisor.
    """
    # Handle edge case where one is zero but not both - though typically "lengths" implies >= 0
    
    def euclid_gcd(a: int, b: int) -> int:
        a = abs(a)
        b = abs(b)
        while b != 0:
            a, b = b, a % b
        return a

    if l1 == 0 and l2 == 0:
        # Undefined ratio for zero lengths. Return (0, 1) or similar as placeholder based on typical reduction behavior where all zeros are treated specially, 
        # but strictly following simplification logic without specific "zero" rules other than GCD behavior which returns non-zero only if inputs weren't both zero.
        # If both are zero, mathematically undefined. Returning (0, 1) acts as an identity for the second part in simplified fraction context often seen in programming challenges 
        # to avoid division by zero logic errors during internal calc before reduction check, but here we do GCD first. 
        # Actually if gcd(0,0)=0, then l1/gcd is div by 0 error.
        return (0, 1) 

    common_divisor = euclid_gcd(l1, l2)
    
    simplified_l1 = l1 // common_divisor
    simplified_l2 = l2 // common_divisor
    
    # Ensure the sign convention: typically ratios are positive for lengths. 
    # If inputs were negative (unlikely for length), we might normalize signs to keep first non-zero positive or similar, 
    # but assuming absolute values as "lengths" implies magnitude only in many contexts unless specified direction matters.
    return (abs(simplified_l1), abs(simplified_l2))

if __name__ == '__main__':
    # Hard-coded sample tests to ensure the function runs without user input, args, or network access
    test_cases = [
        (60, 45),   # Expected output: (4, 3) - GCD is 15 -> 60/15=4, 45/15=3
        (24, 8),    # Expected output: (3, 1) - GCD is 8 -> 24/8=3, 8/8=1
        (7, 14),    # Expected output: (1, 2) - GCD is 7 -> 7/7=1, 14/7=2
        (0, 5),     # Edge case involving zero length part. Assuming reduction keeps it as (0 : simplified). 
                    # If gcd(0,5)=5 -> 0/5=0, 5/5=1 => (0, 1)
        (-60, -45)  # Handling potential negative inputs by taking absolute values in the helper logic effectively. Result: (4, 3)
    ]

    for i, case in enumerate(test_cases):
        result = find_ratio_of_lengths(case[0], case[1])
        print(f"Ratio {case} -> ({result})")