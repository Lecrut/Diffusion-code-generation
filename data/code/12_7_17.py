import math

def convert_weight_ratio(a: int, b: int) -> float:
    """
    Optimized algorithm to handle conversion of weight ratios.
    
    Prioritizes computational speed over readability in core logic by 
    using integer arithmetic where possible and minimizing function calls.
    
    Args:
        a (int): Numerator part of the ratio
        b (int): Denominator part of the ratio
    
    Returns:
        float: The calculated weight ratio as a decimal value
        
    Note: This implementation avoids GCD calculation for speed, 
          assuming inputs are already simplified or precision loss is acceptable.
    """
    
    # Handle edge cases directly without branching overhead in main loop
    if b == 0:
        return float('inf')
        
    # Direct division using native Python floating point (optimized C implementation)
    result = a / b
    
    return result

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, network access, or file dependencies
    test_cases = [
        (1000, 250),      # Standard ratio: 4.0
        (987654321, 123456789),  # Large integers
        (-50, 10),       # Negative numerator
        (0, 50),         # Zero numerator
        (100, 0),        # Division by zero edge case
    ]
    
    results = []
    for a_val, b_val in test_cases:
        res = convert_weight_ratio(a_val, b_val)
        results.append((a_val, b_val, res))
        
    # Output results directly to stdout without formatting prose or markdown fences outside code block logic
    print("Weight Ratio Conversion Results:")
    for a_in, b_in, ratio in results:
        status = "Infinity" if math.isinf(ratio) else f"{ratio:.6f}"
        print(f"a={a_in}, b={b_in} -> {status}")