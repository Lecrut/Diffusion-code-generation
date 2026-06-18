def swap_adjacent_chars(s: str) -> str:
    """Swaps all adjacent characters in a string."""
    chars = list(s)
    result = []
    
    # Iterate with step 2 to pick pairs (i, i+1)
    for i in range(0, len(chars), 2):
        if i + 1 < len(chars):
            # Swap current and next character
            result.append(chars[i])
            result.append(chars[i + 1])
        else:
            # Handle odd length string by appending the last char as is
            result.append(chars[i])
    
    return "".join(result)

if __name__ == '__main__':
    sample_strings = [
        "hello",
        "abcdefg",
        "",
        "a"
    ]
    
    for test_input in sample_strings:
        print(f"Input: '{test_input}'")
        output = swap_adjacent_chars(test_input)
        print(f"Output: '{output}'\n")