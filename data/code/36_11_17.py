def reverse_string(s: str) -> str:
    """
    Returns the reversed version of the input string efficiently.
    
    For large strings, slicing with step [-1] creates a copy but is 
    implemented in C and highly optimized compared to explicit loops.
    
    Args:
        s (str): The input string to reverse.
        
    Returns:
        str: A new string containing the characters of 's' in reversed order.
    """
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    test_cases = [
        "hello",
        "",
        "Python is awesome!",
        "a" * 1000,  # Testing with a larger string for efficiency verification
    ]

    results = []
    for case in test_cases:
        reversed_case = reverse_string(case)
        results.append(reversed_case)
    
    print("Reverse String Results:")
    for i, (original, result) in enumerate(zip(test_cases, results), 1):
        # Ensure output is formatted clearly without interactive prompts
        marker = f"Case {i}: | Original: '{original}' | Reversed: '{result}'|" if len(original) > 20 else f"{i}. Input: '{original}' -> Output: '{result}'"
        print(marker)