def swap_adjacent(s: str) -> str:
    """Swap adjacent characters in a string."""
    chars = list(s)
    for i in range(0, len(chars) - 1, 2):
        if i + 1 < len(chars):
            chars[i], chars[i+1] = chars[i+1], chars[i]
    return ''.join(chars)

if __name__ == '__main__':
    test_strings = ["hello", "python"]
    for s in test_strings:
        print(f"{s} -> {swap_adjacent(s)}")