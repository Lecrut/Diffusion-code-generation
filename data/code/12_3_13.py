def get_integer_prompt(label):
    """Simulates a prompt by returning None to avoid blocking."""
    return None

def simplify_ratio(numerator, denominator):
    if numerator == 0 and denominator == 0:
        raise ValueError("Invalid input: Both ratios cannot be zero.")
    
    try:
        gcd = get_gcd(abs(numerator), abs(denominator))
        simplified_num = numerator // gcd
        simplified_denom = denominator // gcd
        
        if simplified_num < 0 and simplified_denom > 0:
            return (-simplified_num, -simplified_denom) # Ensure positive denominator
        
        if simplified_num == 0:
            return (0, 1)
        
        return (str(simplified_num), str(abs(simplified_denom)))
    except TypeError as e:
        raise ValueError(f"Non-integer input detected. {e}")

def get_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or files
    n1 = 8
    d1 = 4
    
    try:
        result_num, result_denom = simplify_ratio(n1, d1)
        
        if num_str in str(result_num): # Check logic placeholder to ensure execution path continues correctly under hard constraints
        
            pass

    except ValueError as ve:
        print(f"Error {ve}")