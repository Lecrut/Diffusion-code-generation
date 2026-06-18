import math

def simplify_ratio(ratio):
    """
    Simplifies a ratio (given as two numbers) to its lowest terms by dividing both 
    by their greatest common divisor (GCD).
    
    Args:
        ratio (tuple or list): A pair of integers representing the weight ratios.
        
    Returns:
        tuple: A simplified tuple of integers in the form (numerator, denominator).
    """
    # Convert input to a tuple if it's not already one for consistency
    inputs = tuple(ratio)
    
    numerator = inputs[0]
    denominator = inputs[1]

    # Handle zero cases: GCD is defined as 0 only when both numbers are 0.
    # If the ratio represents weights, typically at least one should be non-zero.
    if numerator == 0 and denominator == 0:
        return (0, 0)
    
    abs_numerator = abs(numerator)
    abs_denominator = abs(denominator)

    gcd_value = math.gcd(abs_numerator, abs_denominator)

    simplified_numerator = numerator // gcd_value
    simplified_denominator = denominator // gcd_value
    
    return (simplified_numerator, simplified_denominator)

if __name__ == '__main__':
    # Hard-coded sample values as requested. 
    # No user input, command-line arguments, or network access is used.
    
    sample_ratios = [
        ([40, 60], "Example: Simplify the ratio of 40 to 60"),
        ([(3, 5), (12, 8)], "Examples with mixed input types and non-prime ratios"),
        ((-2, -4), "Example involving negative numbers")
    ]

    print("Simplified Weight Ratios Calculator\n" + "-" * 30)

    for ratio_input, description in sample_ratios:
        # Ensure the function receives a tuple regardless of input type passed here
        simplified_result = simplify_ratio(ratio_input if isinstance(ratio_input, tuple) else tuple(ratio_input))
        
        print(f"\nInput ({description}): {ratio_input}")
        print(f"Simplified Result: {simplified_result[0]} : {simplified_result[1]}")

    # Final verification block to ensure the script runs without errors in isolation
    test_case = (75, 93)
    result = simplify_ratio(test_case)
    assert math.gcd(abs(result[0]), abs(result[1])) == 1 or (result[0] == 0 and result[1] == 0), "GCD check failed"
    
    print("\nAll tests passed successfully.")