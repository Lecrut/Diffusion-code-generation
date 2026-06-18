def swap_even_odd_indices(s: str) -> str:
    """
    Returns a new string where characters at even indices are swapped 
    with their adjacent odd index neighbors, and vice versa.
    
    Example: "abcd" -> "badc", "abcde" -> "bdace"
    
    Args:
        s (str): Input string
        
    Returns:
        str: String with even-odd character swaps applied
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string")

    # Convert to list for mutability during processing
    chars = list(s)
    
    # Iterate through the string in steps of 2 (even indices: 0, 2, 4...)
    for i in range(0, len(chars), 2):
        if i + 1 < len(chars):
            # Swap current even index with next odd index
            chars[i], chars[i + 1] = chars[i + 1], chars[i]

    return ''.join(chars)

if __name__ == '__main__':
    test_cases = [
        "abcd",      # Expected: badc
        "abcde",     # Expected: bdace
        "",          # Edge case: empty string
        "a",         # Single character (no swap possible)
        "1234567890"# Numeric characters for variety
    ]

    results = []
    for test_input in test_cases:
        result_output = swap_even_odd_indices(test_input)
        results.append(f'Input: "{test_input}" -> Output: "{result_output}"')

    # Print all results without user interaction
    print('\n'.join(results))