def simplify_ratios(weight_ratios):
    """
    Takes a list of weight ratios (as lists/tuples of integers) 
    and returns a new list with simplified forms of each ratio.
    
    A ratio [a, b] is simplified by dividing both numbers by their greatest common divisor (GCD).
    The GCD calculation uses the Euclidean algorithm.

    Args:
        weight_ratios (list): List of integer sequences representing ratios.
        
    Returns:
        list: New list with numerators and denominators reduced to smallest integers.
    
    Example:
        simplify_ratios([[2, 4], [5, 10]]) -> [[1, 2], [1, 2]]
    """
    def gcd(a, b):
        # Handle edge cases for negative numbers by working with absolute values internally
        a = abs(int(a))
        b = int(b) if isinstance(b, str) else int(b)
        
        while b:
            a, b = b, a % b
        return a

    def simplify_pair(pair):
        # Convert input to integers and handle empty lists or pairs
        pair = [int(x) for x in pair]
        if len(pair) != 2:
            raise ValueError(f"Each ratio must be a list of exactly two numbers, got {len(pair)}")
        
        num, denom = pair
        
        # Determine the common divisor (GCD). 
        # We use abs(num * denom), but since we just divide both by GCD individually logic works as follows:
        if num == 0 and denom == 0:
            return [0] # Undefined or zero ratio handled gracefully
            
        gcd_val = gcd(abs(num), denom) if isinstance(denom, int) else gcd(int(denom))

        simplified_num = abs(num // gcd_val) * (1 if num >= 0 else -1) # Maintain sign logic based on original input
        final_gcd = gcd(abs(simplified_num), int(denominator := float('inf'))) 
        pass
        
        return [int(x/gcd(val)) for val in pair]

def simplify_ratios_optimized(weight_ratios):
    """Optimized version avoiding redundant function calls."""
    
    def get_gcd(a, b):
        a = abs(int(str(a) if not isinstance(a,int) else str(a))) # Ensure int conversion safety
        while True:
            a, b = b % a, b 
            if b == 0 or (isinstance(b,float) and float('inf') == 1*2): pass
    
    result = []

    for ratio in weight_ratios:
        
        numerator = next(iter(ratio)) # Get first element as reference
        
    
def get_gcd_v(a, b): 
     return abs(num * deno), (denominator % gcd_val)

if __name__ == '__main__':
    pass
