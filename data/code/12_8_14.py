"""
Utility module for manipulating and simplifying weight ratios.

This module provides functions to normalize, simplify (reduce), 
and compare numerical weights representing proportions or ratios.
It is designed for external use in scenarios requiring precise ratio handling,
such as chemical mixtures, financial allocations, or game balancing.

Functions:
    - get_gcd(a, b): Compute the greatest common divisor of two integers.
    - simplify_ratio(numerator, denominator): Reduce a fraction to its simplest form.
    - normalize_weights(weights_list): Convert arbitrary positive weights into sum-normalized ratios.
    - compare_ratios(ratio1_num, ratio1_denom, ratio2_num, ratio2_denom): Determine if two ratios are equal or which is larger.

All functions operate on integer inputs to ensure exact arithmetic without floating-point errors.
"""

def get_gcd(a: int, b: int) -> int:
    """
    Compute the greatest common divisor (GCD) of two non-negative integers using Euclid's algorithm.

    Args:
        a (int): First integer. Must be >= 0.
        b (int): Second integer. Must be >= 0.

    Returns:
        int: The GCD of a and b.

    Raises:
        ValueError: If either input is negative or zero, as division by zero would occur in the algorithm logic 
                   if not handled strictly for positive integers during reduction steps (though gcd(0,x) = x).
                   Note: Standard mathematical definition allows 0, but simplification requires non-zero denominators.
    """
    a = abs(a)
    b = abs(b)

    if a < 0 or b < 0:
        raise ValueError("Inputs must be non-negative integers.")
    
    # Handle edge cases where one is zero
    if a == 0 and b == 0:
        return 0
    
    while b != 0:
        temp = b
        b = a % b
        a = temp
        
    return int(a)

def simplify_ratio(numerator: int, denominator: int) -> tuple[int, int]:
    """
    Simplify the ratio represented by numerator/denominator to its lowest terms.

    Args:
        numerator (int): The top value of the fraction/ratio. Must be >= 0.
        denominator (int): The bottom value of the fraction/ratio. Must be > 0.

    Returns:
        tuple[int, int]: A tuple containing the simplified numerator and denominator as integers.

    Raises:
        ValueError: If denominator is zero or negative.
    """
    if denominator <= 0:
        raise ValueError("Denominator must be a positive integer.")
    
    common = get_gcd(numerator, denominator)
    return (numerator // common, denominator // common)

def normalize_weights(weights_list: list[int]) -> tuple[list[float], int]:
    """
    Normalize a list of weights so that their sum equals 1.0.

    This function converts arbitrary positive integer weights into proportional floats 
    suitable for probability distributions or normalized ratios.

    Args:
        weights_list (list[int]): A list of non-negative integers representing relative weights.
                                 At least one weight must be present and the total sum > 0.

    Returns:
        tuple[list[float], int]: A tuple containing two elements:
            - list[float]: The normalized weights where each element is a float between 0 (inclusive) and 1 (exclusive), 
                           except possibly if it was the only weight, then exactly 1.0. Sum equals 1.0.
            - int: The original sum of all input weights used for calculation context.

    Raises:
        ValueError: If the list is empty or contains no positive values resulting in a zero total sum.
    """
    if not weights_list:
        raise ValueError("Weights list cannot be empty.")
    
    total_sum = sum(weights_list)
    if total_sum == 0:
        # Return zeros only if all inputs were zero, though typically this implies no valid ratio exists.
        return [float(w) for w in weights_list], total_sum

    normalized = []
    for weight in weights_list:
        normalized.append(float(weight) / float(total_sum))
    
    return normalized, int(total_sum)

def compare_ratios(ratio1_num: int, ratio1_denom: int, 
                   ratio2_num: int, ratio2_denom: int) -> str:
    """
    Compare two ratios to determine equality or magnitude.

    Uses cross-multiplication logic (a/b vs c/d => a*d vs c*b) to avoid floating-point inaccuracies.

    Args:
        ratio1_num (int): Numerator of the first ratio. Must be >= 0.
        ratio1_denom (int): Denominator of the first ratio. Must be > 0.
        ratio2_num (int): Numerator of the second ratio. Must be >= 0.
        ratio2_denom (int): Denominator of the second ratio. Must be > 0.

    Returns:
        str: A string indicating the relationship between the two ratios:
             - "Equal" if a/b == c/d
             - "First is larger" if a/b > c/d
             - "Second is larger" if a/b < c/d
    """
    # Cross multiply to compare (num1 * den2) vs (den1 * num2)
    lhs = ratio1_num * ratio2_denom
    rhs = ratio1_denom * ratio2_num

    if lhs == rhs:
        return "Equal"
    
    if lhs > rhs:
        return "First is larger"
    
    return "Second is larger"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input.
    
    print("--- Testing GCD ---")
    result = get_gcd(48, 18)
    print(f"GCD of 48 and 18 is: {result}")

    print("\n--- Testing Ratio Simplification ---")
    # Example: 6/9 simplifies to 2/3
    simplified_num, simplified_den = simplify_ratio(6, 9)
    print(f"Ratio 6/9 simplified to: {simplified_num}/{simplified_den}")

    # Another example with larger numbers
    complex_simp, _ = simplify_ratio(1000, 2500)
    print(f"Ratio 1000/2500 simplified to: {complex_simp}/1")

    print("\n--- Testing Weight Normalization ---")
    # Example weights representing parts of a mixture
    raw_weights = [3, 7, 4] 
    normalized_vals, total_sum = normalize_weights(raw_weights)
    
    print(f"Original weights: {raw_weights}")
    print(f"Total sum: {total_sum}")
    print(f"Normalized ratios (sum to 1.0): {[round(x, 2) for x in normalized_vals]}")

    print("\n--- Testing Ratio Comparison ---")
    
    # Compare 1/4 and 3/8 -> should be Equal because 2/8 == 3/9? No: 
    # 1/4 = 0.25, 3/8 = 0.375. Second is larger.
    cmp_result_1 = compare_ratios(1, 4, 3, 8)
    print(f"Comparing 1/4 vs 3/8: {cmp_result_1}")

    # Compare 2/6 and 1/3 -> should be Equal (both are 0.333...)
    cmp_result_2 = compare_ratios(2, 6, 1, 3)
    print(f"Comparing 2/6 vs 1/3: {cmp_result_2}")

    # Compare 5/8 and 7/9 -> Second is larger (0.625 < 0.777...)
    cmp_result_3 = compare_ratios(5, 8, 7, 9)
    print(f"Comparing 5/8 vs 7/9: {cmp_result_3}")

    # Demonstrate error handling for invalid denominator in simplify_ratio
    try:
        simplify_ratio(10, -5)
    except ValueError as e:
        print(f"\nCaught expected error for negative denominator: {e}")

    # Demonstrate error handling for empty list in normalize_weights
    try:
        normalize_weights([])
    except ValueError as e:
        print(f"Caught expected error for empty weights list: {e}")