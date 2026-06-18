def swap_characters(s: str) -> str:
    """Swaps adjacent pairs of characters in a string in place."""
    if len(s) == 0:
        return s
    
    # Convert list to make mutable operations possible
    chars = list(s)
    
    # Iterate over the list with step size 2
    for i in range(0, len(chars), 2):
        # Check if there is a second character at this position
        if i + 1 < len(chars):
            # Swap current and next character
            chars[i], chars[i + 1] = chars[i + 1], chars[i]
    
    return ''.join(chars)

if __name__ == '__main__':
    sample_strings = [
        "abcdef",
        "",
        "a",
        "xyztuv"
    ]
    
    for original in sample_strings:
        result = swap_characters(original)
        print(f"Original: '{original}' -> Swapped: '{result}'")