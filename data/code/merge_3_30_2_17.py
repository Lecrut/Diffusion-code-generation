def swap_adjacent_pairs(s: str) -> str:
    """Swap all adjacent character pairs within the string."""
    if len(s) % 2 == 1:
        return s
    
    result = []
    i = 0
    while i + 1 < len(s):
        # Swap characters at index i and i+1
        pair = list(s[i:i+2])
        pair.reverse()
        result.extend(pair)
        i += 2
    
    return ''.join(result)

if __name__ == '__main__':
    test_strings = [
        "abcdef",
        "",
        "abcd"
    ]
    
    for input_str in test_strings:
        output_str = swap_adjacent_pairs(input_str)
        print(output_str)