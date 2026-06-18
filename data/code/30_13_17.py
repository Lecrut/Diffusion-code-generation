def swap_adjacent_chars(s: str) -> str:
    """Swaps all adjacent characters in a string."""
    chars = list(s)
    n = len(chars)
    
    # Iterate over even indices and swap with the next character if it exists
    for i in range(0, n - 1, 2):
        chars[i], chars[i + 1] = chars[i + 1], chars[i]
    
    return "".join(chars)

if __name__ == '__main__':
    sample_strings = [
        "abcdef",
        "aabbccdd",
        "",
        "z"
    ]
    
    for test_input in sample_strings:
        result = swap_adjacent_chars(test_input)
        print(f'Input: "{test_input}" -> Output: "{result}"')