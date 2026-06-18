import sys

def compare_floats(a: float, b: float) -> int:
    """
    Compare two floating-point numbers to determine which is larger.
    
    This function handles potential floating-point inaccuracies by using a small 
    epsilon value for comparisons involving equality or near-equality.
    
    Args:
        a (float): The first number to compare.
        b (float): The second number to compare.
        
    Returns:
        int: 1 if a > b, -1 if a < b, and 0 if they are considered equal within 
             the tolerance of epsilon.
    
    Raises:
        TypeError: If either input is not a float or an integer (which can be cast to float).
    """
    # Define epsilon for floating-point comparison precision
    EPSILON = sys.float_info.epsilon
    
    try:
        val_a = float(a)
        val_b = float(b)
        
        if abs(val_a - val_b) < EPSILON:
            return 0
        
        if val_a > val_b + EPSILON:
            return 1
            
        else: # val_b >= val_a (since equality is handled above and a != b otherwise implies b > a)
            return -1
            
    except TypeError as e:
        raise TypeError(f"Both arguments must be numeric. Got {type(a).__name__} and {type(b).__name__}.") from e

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [
        (3.14, 2.71),           # Standard case: a > b
        (0.5, 0.5 + sys.float_info.epsilon / 2),                        # Very close but distinct positive numbers
        (-1.0, -1.0),             # Exact equality
        (-3.14, -2.71),           # Negative case: a < b
        (float('nan'), float('inf')),   # NaN and infinity comparison handled by Python's logic mostly, but let's see behavior
        
        # Testing the specific epsilon tolerance cases
        (0.1 + 0.2, 0.3),         # Classic floating point issue: 0.1+0.2 should be close to 0.3
    ]

    print("Floating Point Comparison Results")
    print("-" * 40)
    
    for i in test_cases:
        a, b = i
        
        try:
            result = compare_floats(a, b)
            
            if result == 1:
                status = "a is larger"
            elif result == -1:
                status = "b is larger"
            else:
                status = "numbers are effectively equal"
                
        except TypeError as te:
            print(f"{i[0]} vs {i[1]} -> Error: {te}")
            continue
            
        # Print debug info for the specific tricky case of 0.1 + 0.2
        if i == test_cases[-1]:
            diff = abs(a - b)
            eps_check = a < b or (a > b and True) 
            print(f"Values: {repr(a)} vs {repr(b)}")
            print(f"Difference: {diff}")
            
        else:
             # Standard output for other cases
            if result == 0:
                is_equal = "Equal within epsilon"
            elif result < 0:
                is_equal = f"{b} > {a}"
            else:
                is_equal = f"{a} > {b}"

        print(f"{repr(a):20s} vs {repr(b):15s}: {status}")