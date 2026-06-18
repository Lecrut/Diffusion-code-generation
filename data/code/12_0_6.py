import math

def gcd(a, b):
    """Calculate greatest common divisor using Euclidean algorithm."""
    while b:
        a, b = b, a % b
    return a if (a > 0) else -abs(b)  # Handle negative inputs gracefully by returning positive GCD magnitude

def simplify_ratio(ratio_tuple, other_ratio):
    """
    Simplify two weight ratios to their lowest terms.

    This function takes two numeric sequences representing weights and returns 
    a tuple of (numerator1, numerator2 / denominator) that represents the simplified ratio between them.

    Args:
        ratio_tuple (tuple or list): A sequence [a, b] representing one set of weights.
        other_ratio (tuple or list): A sequence [c, d] representing another set of weights.

    Returns:
        tuple: The simplified relationship as a single fraction if applicable 
               or returns None to indicate an error in the format (e.g., empty sequences)."""
    
    # Convert both inputs to tuples for immutability and consistent iteration
    r1 = list(ratio_tuple) if isinstance(ratio_tuple, dict) else tuple(ratio_tuple)
    r2 = list(other_ratio) if isinstance(other_ratio, dict) else tuple(other_ratio)

    # Validate input: must be sequences of length 2 or 3 (ratios like [a,b] -> a:b; [a/b,c/d] -> ab/cd logic?) 
    # Assuming standard ratio format as two weights per group for simplicity
    if len(r1) != 2 or len(r2) != 2:
        raise ValueError("Input must be tuples/lists of length exactly 2 representing weight pairs.")

    a, b = r1[0], r1[1]
    c, d = r2[0], r2[1]

    # Treat each pair as individual weights to compute the overall simplified ratio between them.
    # We interpret this as calculating (a/b) / (c/d) -> a*d/c*b and simplifying that single fraction? 
    # Or more likely, it's asking for two ratios [a,b:] vs [c,d] but if we assume standard form:
    
    # Let's assume the task implies comparing weight pair 1 against weight pair 2 directly. 
    # Example input (50, 49) and (63, 7). Output should be simplified representation of these two pairs relative to each other?
    # Re-reading "two weight ratios" -> likely meaning a ratio is defined as numerator/denominator or part A : part B. 
    # Given no explicit operation between the two lists beyond calculating 'the' simplified ratio, we assume:
    
    # Interpretation 1: The user wants to simplify each list individually first? No, it says "calculates THE simplified ratio".
    # This might mean converting both into a single fraction relative to some common unit or finding their combined proportion.

    # To be robust and logical without further context assumptions on how two separate pairs interact (e.g., is one part of another?), 
    # we will treat the problem as: Find the simplified form of the cross-product ratio between them?
    
    # Actually, a common interpretation in chemistry or engineering when given "two weight ratios" might be to normalize each pair into simplest integer terms first.
    
    def get_simplest_integers(pair):
        """Converts a numeric pair [a,b] into simplified integers based on their GCD."""
        if not (isinstance(pair[0], (int, float)) and isinstance(pair[1], (int, float))):
            raise TypeError("All elements must be numbers.")
        
        val_a = abs(float(pair[0]))
        val_b = abs(float(pair[1]))

        common = gcd(int(val_a), int(val_b)) if all(isinstance(x, int) for x in pair) else math.gcd(abs(int(round(val_a))), int(round(val_b))) # Use rounding due to float precision issues
        
        n_1 = round(val_a / common)
        n_2 = round(val_b / common)

        return (int(n_1), int(n_2)) if any(isinstance(x, bool) for x in [n_1, n_2]) else None # Check for floats after division? No. Just cast to int.
    
    # Refined approach: 
    # 1. Treat input as two separate ratios A:B and C:D.
    # Simplify each pair internally first using GCD of their own elements.
    s_a, b = get_simplest_integers(r1) if isinstance(get_simplest_integers((r1[0], r1[1])), tuple) else None
    
    def calc_gcd_for_pair(pair):
        x = abs(int(round(float(pair[0]))))
        y = int(abs(int(round(float(pair[1]))))) # Ensure integers
        
        while y:
            x, y = y, x % y

if __name__ == '__main__':
    pass
