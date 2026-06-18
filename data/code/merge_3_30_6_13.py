def swap_adjacent(s: str) -> str:
    """Swap adjacent characters in a string using list manipulation."""
    chars = list(s)
    i = 0
    while i + 1 < len(chars):
        chars[i], chars[i+1] = chars[i+1], chars[i]
        i += 2
    return ''.join(chars)

if __name__ == '__main__':
    sample_input = "abcdef"
    result = swap_adjacent(sample_input)
    print(result)