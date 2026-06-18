import sys

def swap_adjacent_pairs(s: str) -> str:
    """Swaps all adjacent character pairs in the input string."""
    result = []
    i = 0
    length = len(s)
    
    while i < length - 1:
        if i + 2 <= length and s[i] != '':
            # Swap current pair with next char, then move two steps forward
            first_char, second_char = s[i], s[i+1]
            result.append(second_char)
            result.append(first_char)
            i += 2
    
    return ''.join(result)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or command-line arguments
    test_cases = [
        "ab",
        "abcdefg",
        "",
        "!@#$"
    ]
    
    for case in test_cases:
        modified_string = swap_adjacent_pairs(case)
        print(modified_string)