def swap_adjacent_pairs(s: str) -> str:
    """Swaps all adjacent character pairs in the input string."""
    if len(s) == 0 or len(s) % 2 != 0:
        return s
    
    result = []
    
    for i in range(0, len(s), 2):
        # Swap characters at index i and i+1 if they exist
        if i + 1 < len(s):
            result.append(s[i + 1])
            result.append(s[i])
        else:
            result.append(s[i])
            
    return ''.join(result)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input
    test_cases = [
        "abcdef",
        "1234567890",
        "",
        "a",
        "ab"
    ]
    
    for test_input in test_cases:
        output = swap_adjacent_pairs(test_input)
        print(output)