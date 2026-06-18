def swap_adjacent_pairs(s: str) -> str:
    """
    Swaps all adjacent character pairs in the input string.
    
    If the length is odd, the last character remains unchanged.
    Example: "abcd" becomes "badc", "abcde" becomes "bcdae".
    """
    result = []
    i = 0
    
    while i < len(s):
        if i + 1 < len(s):
            # Swap the pair (s[i], s[i+1]) -> append in reverse order
            result.append(s[i + 1])
            result.append(s[i])
            i += 2
        else:
            # Odd length case: keep the last character as is
            result.append(s[i])
            i += 1
    
    return ''.join(result)

if __name__ == '__main__':
    sample_strings = [
        "abcdef",
        "a",
        "",
        "xyztuvw"
    ]
    
    for test_input in sample_strings:
        output_str = swap_adjacent_pairs(test_input)
        print(output_str)