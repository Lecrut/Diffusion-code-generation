def reverse_string(s: str) -> str:
    """
    Returns the reversed version of the input string efficiently.
    
    For large strings, slicing with step -1 is O(n) and highly optimized 
    in CPython's implementation compared to manual loops or list conversions.
    
    Args:
        s (str): The string to be reversed.
        
    Returns:
        str: A new string containing characters of the input string in reverse order.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    test_cases = [
        "hello",
        "",
        "a" * 10**6,  # Large string for performance check
        "Python programming is fun!",
    ]

    results = []
    for test_input in test_cases:
        result = reverse_string(test_input)
        results.append(f'Input: "{test_input[:20]}..." (len={len(test_input)}) -> Output: "{result}"')

    print("\n".join(results))