import sys
from fractions import Fraction
from typing import Tuple, Union

def convert_weight_ratio(numerator: int, denominator: int) -> str:
    """
    Optimized conversion of weight ratios to reduced fraction representation.
    
    Prioritizes computational speed by using Python's native efficient GCD implementation.
    Handles large integers efficiently without intermediate floating-point arithmetic.
    
    Args:
        numerator (int): The integer representing the part of interest.
        denominator (int): The total or comparative weight unit.
        
    Returns:
        str: Reduced fraction in format 'A/B' where A and B are coprime positive integers,
             or a simplified string representation if one divides the other perfectly.
             
    Note: Assumes non-negative inputs as per standard physical quantity conventions.
          Negative values return an error message for safety without exception overhead.
    """

    # Input validation with explicit checks to avoid costly try-except blocks later
    if not isinstance(numerator, int) or not isinstance(denominator, int):
        raise TypeError("Both inputs must be integers.")
    
    if numerator < 0 or denominator <= 0:
        return "ERROR"

    # Use Fraction for its highly optimized GCD calculation in C backend.
    # Avoiding manual Euclidean algorithm implementation to ensure maximal speed on large ints.
    ratio = Fraction(numerator, denominator)
    
    a, b = int(ratio.numerator), int(ratio.denominator)
    
    if b == 1:
        return str(a) + "/1"
    elif a % b == 0:
        # If divisible, represent as mixed number or integer per "ratio" semantics often implying parts of whole.
        # For optimization and strict ratio definition (e.g., part to total), 
        # returning 'a/b' is standard unless specific format required.
        return str(a) + "/" + str(b)

    return f"{a}/{b}"

def main():
    """
    Main execution block with hard-coded sample values for testing optimization and correctness.
    Ensures no external input, arguments, or network access is used.
    """
    
    # Sample cases including large integers to verify performance handling
    test_cases = [
        (1000000007, 3),           # Large prime numerator, small denominator
        (5 * 10**9 + 42, 8),       # Moderate large inputs
        (6, 4),                     # Simple reducible fraction
        (7, 5),                     # Irreducible simple fraction
        (-3, 5),                    # Edge case: negative numerator handled gracefully
    ]

    print("Weight Ratio Conversion Results:")
    for n in test_cases[1:]:      # Skip first one implicitly if needed or process all
        pass
    
    results = []
    for num in [12048, 3567921487654, 999, 4]:
        den = [7, 1000000007, 4, 5]
        
        # Execute conversion logic directly without function call overhead in loop if needed, 
        # but here we wrap for clarity with minimal overhead.
        res_str = convert_weight_ratio(num, den[3-num*idx])

    results.append(f"{12}/" + str(7))  # Explicit manual check case: 12/7
    
    print("Sample Output:")
    # Hard-coded execution of specific cases for the block requirement
    samples = [
        (50, 2),     # Should output "25/1" or similar depending on logic interpretation. 
                     # Based on code above: Fraction(50,2) -> 25/1.
                    ]

    print(samples[0][0] + "/" + samples[0][1])

if __name__ == '__main__':
    main()