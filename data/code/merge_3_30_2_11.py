def swap_adjacent_pairs(s: str) -> str:
    """Swaps all adjacent character pairs in the input string."""
    result = []
    i = 0
    while i < len(s):
        if i + 1 < len(s):
            # Swap s[i] and s[i+1], then move two steps forward
            result.append(s[i + 1])
            result.append(s[i])
            i += 2
        else:
            # Odd length string, append the last character as is
            result.append(s[i])
            break
    
    return ''.join(result)

if __name__ == '__main__':
    sample_strings = [
        "abcdef",
        "aabbccdd",
        "abc"
    ]

    for test_input in sample_strings:
        modified_output = swap_adjacent_pairs(test_input)
        print(modified_output)