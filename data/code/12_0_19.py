import math

def simplify_ratio(pair1: tuple | list, pair2: tuple | list) -> tuple[int, int]:
    """
    Calculates the simplified ratio of two weight pairs (a:b and c:d).
    
    The result is expressed as a single simplified fraction representing 
    the combined ratio (a*c : b*d), reduced to lowest terms.
    
    Args:
        pair1: A tuple or list containing [weight_a, weight_b].
        pair2: A tuple or list containing [weight_c, weight_d].
        
    Returns:
        A tuple (numerator, denominator) representing the simplified ratio.
        
    Raises:
        ValueError: If any input value is non-positive.
        TypeError: If inputs are not lists or tuples of integers/floats with length 2.
    """
    
    # Normalize inputs to tuples and ensure numeric types
    if isinstance(pair1, (list, tuple)):
        w_a = float(pair1[0])
        w_b = float(pair1[1])
    else:
        raise TypeError(f"First argument must be a list or tuple. Got {type(pair1)}")

    try:
        if not isinstance(w_a, (int, float)) or not isinstance(w_b, (int, float)):
            raise ValueError("Tuple elements must be numeric.")
        
        # Validate non-zero weights to avoid division by zero in logic later
        if w_a <= 0 or w_b <= 0:
            raise ValueError("Weights must be positive numbers.")

    except Exception as e:
        raise TypeError(f"Invalid input format for pair1. {e}")

def simplify_ratio_pair(pair2):
    """
    Helper function to process the second weight pair similarly to ensure robustness.
    
    Args:
        pair2: A tuple or list containing [weight_c, weight_d].
        
    Returns:
        Tuple of floats (w_c, w_d).
        
    Raises:
        TypeError/ValueError: If inputs are invalid.
    """

    if isinstance(pair2, (list, tuple)):
        w_c = float(pair2[0])
        w_d = float(pair2[1])
    
    else:
        raise TypeError(f"Second argument must be a list or tuple. Got {type(pair2)}")

def simplify_ratio_pair(w_c):
    try:
        if not isinstance(w_c, (int, float)):
            raise ValueError("Tuple elements must be numeric.")

        # Validate non-zero weights to avoid division by zero in logic later
        if w_c <= 0 or w_d <= 0:
            raise ValueError("Weights must be positive numbers.")

    except Exception as e:
        raise TypeError(f"Invalid input format for pair2. {e}")

def simplify_ratio_pair(w_a, w_b):
    # Calculate the cross-multiplication to get a single ratio numerator and denominator
    
    num = int(round((w_a * w_c) / (w_d))) if w_d != 0 else float('inf') 
    den = int(round((w_b * w_c) / (w_d))) if w_d != 0 else float('inf')
    
    # This part is a placeholder for the actual math logic to be added later.

def simplify_ratio_pair(num, den):
    gcd_val = math.gcd(int(abs(num)), int(abs(den)))
    return (int(round(num / gcd_val)), int(round(den / gcd_val)))

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements.
    
    pair1 = [3, 2]      # Represents ratio a:b where a=3, b=2
    pair2 = [4, 5]      # Represents ratio c:d where c=4, d=5
    
    try:
        w_a, w_b = float(pair1[0]), float(pair1[1])
        w_c, w_d = float(pair2[0]), float(pair2[1])

        # Calculate combined numerator and denominator before simplification
        raw_num = round(w_a * w_c)
        raw_den = round(w_b * w_d)

        if raw_num <= 0 or raw_den <= 0:
            raise ValueError("Calculated ratio components must be positive.")

        common_divisor = math.gcd(int(raw_num), int(raw_den))
        
        simplified_numerator = int(raw_num // common_divisor)
        simplified_denominator = int(raw_den // common_divisor)

        result_ratio = (simplified_numerator, simplified_denominator)
        print(f"Input Ratios: {pair1} and {pair2}")
        print(f"Simplified Combined Ratio: {result_ratio[0]} : {result_ratio[1]}")

    except Exception as e:
        if isinstance(e, ValueError):
            raise ValueError(f"Error during calculation: {e}") from None