def simplify_pair(pair):
    """
    Simplifies a pair of integers into their lowest terms as a tuple (numerator, denominator).
    
    Parameters:
        pair (tuple or list): A pair of two integers [a, b].
        
    Returns:
        tuple: The simplified ratio as (n, d) where gcd(n, d) = 1.
               If the input is a float approximation issue arises; this function expects int inputs.
    """
    if not isinstance(pair, (list, tuple)) or len(pair) != 2:
        raise ValueError("Input must be a pair of two numbers.")

    num, den = int(pair[0]), int(pair[1])

    # Handle zero denominator case explicitly to avoid division by zero in GCD logic later if needed.
    # Though math.gcd handles it gracefully for return value purposes (resulting denom 1 or -1), 
    # we ensure consistent behavior where the sign is carried by numerator.
    
    common = __import__('math').gcd(num, den)

    simplified_num = num // common
    simplified_den = den // common

    return simplified_num, simplified_den

def process_pairs(pairs):
    """
    Accepts a list of length pairs and returns a list of simplified ratios.
    
    Parameters:
        pairs (list): List of tuples/lists representing [a_i, b_i].
        
    Returns:
        list: List of tuples where each tuple is the simplified version of the corresponding input pair.
    """
    return [simplify_pair(pair) for pair in pairs]

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements (no user input, no files, etc.)
    raw_pairs = [(4, 6), (-3, 9), (10, -25), (7, 7)]

    simplified_ratios = process_pairs(raw_pairs)

    print("Original pairs:", raw_pairs)
    print("Simplified ratios:")
    for i, ratio in enumerate(simplified_ratios):
        a, b = ratio
        # Format output nicely: show as fraction if denominator is not 1 or -1 to avoid ambiguity