def determine_larger(value1: float, value2: float) -> float:
    """
    Returns the larger of two comparable numeric values (int or float).
    
    Args:
        value1: The first numeric value.
        value2: The second numeric value.
        
    Returns:
        The greater of the two input values as a float.
    """
    return max(value1, value2)

if __name__ == '__main__':
    # Sample test cases with various data types and scenarios
    sample_cases = [
        (5, 10),          # Integers: expects 10
        (-3, -7),         # Negative integers: expects -3
        (2.5, 4.8),       # Floats: expects 4.8
        (float('inf'), float('-inf')),  # Infinity cases: expects inf
    ]

    for i in range(len(sample_cases)):
        val1, val2 = sample_cases[i]
        result = determine_larger(val1, val2)
        print(f"Case {i+1}: max({val1}, {val2}) = {result}")