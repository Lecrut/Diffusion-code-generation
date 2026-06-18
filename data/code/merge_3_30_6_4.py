def swap_adjacent_chars(s: str) -> str:
    """Swaps adjacent characters in a string using list manipulation."""
    chars = list(s)
    
    # Swap every pair of adjacent elements (0,1), (2,3), etc.
    for i in range(0, len(chars) - 1, 2):
        if i + 1 < len(chars):
            chars[i], chars[i+1] = chars[i+1], chars[i]
    
    return ''.join(chars)

if __name__ == '__main__':
    sample_strings = ["hello", "pythonic"]
    for s in sample_strings:
        print(f"{s} -> {swap_adjacent_chars(s)}")