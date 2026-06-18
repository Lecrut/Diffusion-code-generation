def swap_adjacent_chars(s: str) -> str:
    """Swaps all adjacent characters in a string."""
    # Convert to list of characters, slice with step 2 starting at index 1 and length -1 (to exclude last char if odd),
    # then interleave back into the original structure.
    chars = list(s)
    
    for i in range(0, len(chars) - 1, 2):
        chars[i], chars[i + 1] = chars[i + 1], chars[i]
        
    return "".join(chars)

if __name__ == '__main__':
    test_cases = [
        "hello",
        "abcdefg",
        "",
        "a"
    ]
    
    for case in test_cases:
        print(f"{case!r} -> {swap_adjacent_chars(case)!r}")