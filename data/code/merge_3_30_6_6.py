def swap_adjacent_chars(s: str) -> str:
    """Swap adjacent characters in a string."""
    chars = list(s)
    for i in range(0, len(chars), 2):
        if i + 1 < len(chars):
            chars[i], chars[i + 1] = chars[i + 1], chars[i]
    return ''.join(chars)

if __name__ == '__main__':
    sample_input = "abcdef"
    result = swap_adjacent_chars(sample_input)
    print(result)