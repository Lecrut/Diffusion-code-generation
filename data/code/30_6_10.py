def swap_adjacent_chars(s: str) -> str:
    """Swap adjacent characters in a string using list manipulation."""
    chars = list(s)
    n = len(chars)
    # Swap pairs of indices (0,1), (2,3), etc.
    for i in range(0, n - 1, 2):
        if i + 1 < n:
            chars[i], chars[i + 1] = chars[i + 1], chars[i]
    return "".join(chars)

if __name__ == '__main__':
    sample_str = "abcdef"
    result = swap_adjacent_chars(sample_str)
    print(result)