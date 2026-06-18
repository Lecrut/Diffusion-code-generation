def swap_adjacent_chars(s: str) -> str:
    """Swaps all adjacent characters in a string."""
    chars = list(s)
    result = []
    
    # Iterate through the list with step 2 to pick pairs
    for i in range(0, len(chars), 2):
        if i + 1 < len(chars):
            # Swap current and next character
            result.append(chars[i])
            result.append(chars[i + 1])
        else:
            # Handle odd length string by appending the last char as is (or swap with itself)
            result.append(chars[i])

    return "".join(result)

if __name__ == '__main__':
    sample_strings = [
        "hello",
        "abcdefg",
        "",
        "a"
    ]
    
    for test_str in sample_strings:
        swapped_result = swap_adjacent_chars(test_str)
        print(f'Original: "{test_str}" -> Swapped: "{swapped_result}"')