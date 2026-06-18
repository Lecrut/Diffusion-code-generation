def swap_adjacent_chars(s: str) -> str:
    """Swaps adjacent characters in a string."""
    chars = list(s)
    for i in range(len(chars) - 1, 0, -2):
        chars[i], chars[i-1] = chars[i-1], chars[i]
    return ''.join(chars)

if __name__ == '__main__':
    test_strings = ["abc", "aabbccdd"]
    for s in test_strings:
        print(f"{s} -> {swap_adjacent_chars(s)}")