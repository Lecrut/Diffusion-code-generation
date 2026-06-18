def swap_adjacent_chars(s: str) -> str:
    """Swap adjacent characters in a string using list manipulation."""
    chars = list(s)
    n = len(chars)
    # Swap pairs (0,1), (2,3), etc. if they exist
    for i in range(0, n - 1, 2):
        chars[i], chars[i + 1] = chars[i + 1], chars[i]
    return ''.join(chars)

if __name__ == '__main__':
    sample_input = "abcdef"
    result = swap_adjacent_chars(sample_input)
    print(result)