def swap_even_odd_indices(s: str) -> str:
    """
    Returns a new string where characters at even indices are swapped 
    with their adjacent odd-indexed neighbors (i.e., s[i] <-> s[i+1]).
    
    The function uses list comprehension and immutability to demonstrate 
    functional programming principles. It avoids modifying the input string in place.

    Args:
        s (str): Input string.

    Returns:
        str: New string with swapped adjacent characters at even-odd indices.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")

    # Convert to list for mutability during processing, then join back to str
    chars = list(s)
    
    # Iterate through the string with step 2 starting from index 0.
    # At each even index i, swap characters at i and i+1 if they exist.
    n = len(chars)
    for i in range(0, n - 1, 2):
        chars[i], chars[i + 1] = chars[i + 1], chars[i]

    return "".join(chars)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    test_cases = [
        "abcdef",      # Expected: 'bdceaf' (a<->b, c<->d, e<->f)
        "hello world", # Expected: 'hleol wrdo d'
        "",            # Edge case: empty string
        "x"             # Single character remains unchanged as there is no pair.
    ]

    for test_input in test_cases:
        result = swap_even_odd_indices(test_input)
        print(f"Input:    '{test_input}'")
        print(f"Output:   '{result}'")
        print("---")