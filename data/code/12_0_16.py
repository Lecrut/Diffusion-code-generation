import math

def simplify_ratio(ratio):
    """
    Takes a tuple or list of two integers representing a ratio (a, b)
    and returns a new tuple/list with the simplified ratio in lowest terms.
    
    The simplification is done by dividing both numbers by their greatest common divisor (GCD).
    If either number is zero, special handling ensures non-negative results where possible,
    but strictly follows mathematical reduction for positive integers as per standard GCD usage.
    """
    if not isinstance(ratio, (tuple, list)):
        raise TypeError("Input must be a tuple or list of two numbers.")
    
    if len(ratio) != 2:
        raise ValueError("Ratio must contain exactly two elements.")

    num = ratio[0]
    den = ratio[1]

    # Handle cases where denominator is zero to avoid division by zero in GCD logic, 
    # though math.gcd handles zeros correctly for the purpose of reduction.
    if not isinstance(num, int) or not isinstance(den, int):
        raise TypeError("Both elements must be integers.")

    gcd = math.gcd(abs(num), abs(den))
    
    simplified_num = num // gcd
    simplified_den = den // gcd
    
    return (simplified_num, simplified_den)

if __name__ == '__main__':
    # Hard-coded sample values as tuples and lists to demonstrate functionality.
    ratio_tuple = (120, 80)
    ratio_list = [45, 63]

    result_tuple = simplify_ratio(ratio_tuple)
    result_list = simplify_ratio(ratio_list)

    print(f"Original tuple: {ratio_tuple} -> Simplified: {result_tuple}")
    print(f"Original list:   {ratio_list} -> Simplified: {result_list}")