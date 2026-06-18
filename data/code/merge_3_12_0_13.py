import math

def simplify_ratio(ratio1: tuple | list, ratio2: tuple | list) -> tuple[int, int]:
    """
    Calculates the simplified ratio of two weight inputs in their lowest terms.
    
    Args:
        ratio1 (tuple or list): First set of weights as a sequence of numbers.
        ratio2 (tuple or list): Second set of weights as a sequence of numbers.
        
    Returns:
        tuple[int, int]: A tuple containing the simplified numerator and denominator 
                         representing the overall weight ratio in lowest terms.
    
    The function computes the sum of each input to get total parts for that side,
    then finds their greatest common divisor (GCD) to simplify the resulting fraction.
    """
    # Convert inputs to lists if they are tuples for consistent processing
    r1 = list(ratio1)
    r2 = list(ratio2)

    # Calculate total parts for each side by summing all weights in their respective sets
    total_r1 = sum(r1)
    total_r2 = sum(r2)

    if total_r1 == 0 or total_r2 == 0:
        raise ValueError("At least one of the weight totals must be greater than zero.")

    # Compute GCD to simplify the ratio between the two totals
    common_divisor = math.gcd(total_r1, total_r2)

    simplified_numerator = total_r1 // common_divisor
    simplified_denominator = total_r2 // common_divisor

    return (simplified_numerator, simplified_denominator)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    weight_set_a = [30, 45]      # Example: parts of a mixture
    weight_set_b = [20, 60]      # Another example set

    result_ratio = simplify_ratio(weight_set_a, weight_set_b)
    
    print(f"Input Set A (weights): {weight_set_a}, Total Parts: {sum(weight_set_a)}")
    print(f"Input Set B (weights): {weight_set_b}, Total Parts: {sum(weight_set_b)}")
    print(f"Simplified Ratio in Lowest Terms: {result_ratio[0]} : {result_ratio[1]}")

    # Additional test case with single values to ensure robustness
    weight_set_c = [5]
    weight_set_d = [2, 3]
    
    result_ratio_2 = simplify_ratio(weight_set_c, weight_set_d)
    print(f"Test Case - Input Set C: {weight_set_c}, Total Parts: {sum(weight_set_c)}")
    print(f"Test Case - Input Set D: {weight_set_d}, Total Parts: {sum(weight_set_d)}")
    print(f"Simplified Ratio (Case 2): {result_ratio_2[0]} : {result_ratio_2[1]}")