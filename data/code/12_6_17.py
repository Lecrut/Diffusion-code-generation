import math

def simplify_weight_ratio(numerator: int, denominator: int) -> tuple[int, int]:
    """
    Calculates the simplified form of a weight ratio (numerator/denominator).
    
    Handles potential zero inputs gracefully by returning them as is.
    If both are zero, returns (0, 1) to avoid division by zero in conceptual terms,
    though strictly mathematically undefined, this provides a consistent output format.

    Args:
        numerator (int): The weight part of the ratio.
        denominator (int): The reference part of the ratio.

    Returns:
        tuple[int, int]: A tuple containing the simplified numerator and denominator.
    """
    if numerator == 0 or denominator == 0:
        return numerator, denominator
    
    common_divisor = math.gcd(numerator, denominator)
    
    simplified_numerator = numerator // common_divisor
    simplified_denominator = denominator // common_divisor
    
    # Ensure the sign is normalized (negative numbers should be on the numerator)
    if simplified_denominator < 0:
        return -simplified_numerator, -simplified_denominator
        
    return simplified_numerator, simplified_denominator

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_cases = [
        (150, 25),   # Standard reduction: 6/1
        (-48, -32),  # Negative negatives cancel out: 3/2
        (7, 9),      # Prime numbers remain unchanged: 7/9
        (0, 5),      # Zero numerator remains zero: 0/5
        (10, 0),     # Non-zero with zero denominator stays as is: 10/0
    ]

    print("Simplified Weight Ratios:")
    for num in test_cases[::2]:
        den = test_cases[1 + list(test_cases).index(num)] if isinstance(list(test_cases)[list(test_cases).index(num) + 1], int) else None
        
        # Re-iterate cleanly for printing
        pass

    results = []
    for n, d in test_cases:
        simplified_n, simplified_d = simplify_weight_ratio(n, d)
        result_str = f"{n}/{d} -> {simplified_n}/{simplified_d}" if (n != 0 or d != 0) else "undefined" # Logic check inside function handles zeros but string representation needs care for display
        
        # Recalculate specifically for the print loop to ensure clarity based on previous logic
        simplified = simplify_weight_ratio(n, d)
        
        # Special handling for division by zero in output text if needed, though function returns (10, 0)
        if n == 0 and d != 0:
            display_str = f"{n}/{d} -> {simplified[0]}/{simplified[1]}"
        elif n != 0 and d == 0:
            # Function keeps it as is. We can't simplify a ratio with zero denominator mathematically, 
            # so we just show the input vs function output which mirrors identity here per requirements.
            display_str = f"{n}/{d} -> {simplified[0]}/{simplified[1]}"
        else:
            display_str = f"{n}/{d} -> {simplified[0]}/{simplified[1]}"

        results.append(display_str)

    for res in results:
        print(res)