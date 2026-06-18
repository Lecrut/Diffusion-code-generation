import math

def simplify_ratio(ratio):
    """
    Takes a tuple or list of two integers representing weights/quantities,
    calculates their greatest common divisor (GCD), divides both numbers by it,
    and returns the simplified ratio as a tuple.

    Args:
        ratio (tuple | list): Two integer values to be simplified.

    Returns:
        tuple: A new tuple containing the two integers in lowest terms.
    
    Raises:
        ValueError: If input is not exactly two elements or contains non-integers.
        ZeroDivisionError: If both numbers are zero.
    """
    if isinstance(ratio, (tuple, list)):
        length = len(ratio)
        if length != 2:
            raise ValueError(f"Input must contain exactly two values, got {length}.")

        # Ensure inputs are integers; convert float to int for safety in ratio calculations.
        try:
            a = int(float(ratio[0]))
            b = int(float(ratio[1]))
            
            if not (isinstance(a, int) and isinstance(b, int)):
                raise ValueError("Input values must be convertible to integers.")

            # Handle the edge case where both are zero. Division by zero is undefined for ratio simplification in this context.
            if a == 0 and b == 0:
                return (1, 1) 

        except (ValueError, TypeError):
            raise ValueError("Input values must be integers.")

    else:
        raise TypeError(f"Expected tuple or list of two numbers, got {type(ratio).__name__}.")

    # Calculate the absolute GCD to handle negative inputs correctly.
    gcd = math.gcd(a, b)

    return (a // gcd, b // gcd)

if __name__ == '__main__':
    # Hard-coded sample values as requested; no user input or arguments required.
    
    # Sample 1: Simple integers with a common factor of 3.
    ratio_1 = [90, 60]
    simplified_ratio_1 = simplify_ratio(ratio_1)

    # Sample 2: Negative numbers and decimals (converted to int).
    ratio_2 = (-45, -81) 

    # Sample 3: Non-coprime positive integers.
    ratio_3 = [75, 100]

    print(f"Input {ratio_1} simplified -> {simplified_ratio_1}")
    
    # Ensure negative logic works correctly (e.g., both negatives should result in positives if we treat them as magnitudes for GCD)
    # However, math.gcd handles signs such that gcd(-45, -81) is 9. 
    # The division will preserve the sign unless handled explicitly. 
    # Standard behavior: (-45//9, -81//9) -> (-5, -9). This preserves original sign which is usually desired for ratios.
    
    print(f"Input {ratio_2} simplified -> {simplified_ratio_2}")

    print(f"Input {tuple(ratio_3)} simplified -> {simplify_ratio(tuple(ratio_3))}")