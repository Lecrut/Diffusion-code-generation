def swap_characters(s: str) -> str:
    """
    Swaps adjacent pairs of characters in a string in place (by returning the modified string).
    
    Args:
        s (str): The input string to modify
        
    Returns:
        str: The modified string with swapped adjacent pairs

    Example:
        >>> swap_characters("abcd")
        'badc'
        >>> swap_characters("abcde")
        'bacde'
    """
    # Convert the string to a list of characters since strings are immutable in Python
    chars = list(s)
    
    # Iterate through the list with step 2 and swap adjacent pairs
    for i in range(0, len(chars), 2):
        if i + 1 < len(chars):
            chars[i], chars[i + 1] = chars[i + 1], chars[i]
    
    # Join the list back into a string to simulate "in-place" modification and return it
    result = "".join(chars)
    return result

if __name__ == '__main__':
    # Hard-coded sample values ensuring no input(), sys.stdin, argparse or network access is needed
    test_cases = [
        ("abcdef",),      # Even length full swap
        ("abcde",),       # Odd length (last char remains)
        ("1234567890"),  # Numbers as characters
        "",               # Empty string edge case
        "a"               # Single character edge case
    ]

    for input_str in test_cases:
        output = swap_characters(input_str[0])
        print(f"Input: '{input_str}' -> Output: '{output}'")