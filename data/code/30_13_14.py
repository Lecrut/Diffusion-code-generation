def swap_adjacent_chars(s: str) -> str:
    """Swaps all adjacent characters in a string."""
    if len(s) <= 1:
        return s
    
    result = []
    
    # Iterate through the string with step of 2 to avoid index errors on odd lengths
    for i in range(0, len(s), 2):
        # Append current character and next character (if exists) swapped
        if i + 1 < len(s):
            result.append(f"{s[i+1]}{s[i]}")
        else:
            result.append(s[i])
    
    return "".join(result)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files
    test_cases = [
        "abcdef",      # Even length string
        "abc",         # Odd length string
        "",            # Empty string
        "a"            # Single character string
    ]

    for text in test_cases:
        swapped_text = swap_adjacent_chars(text)
        print(f"Original: '{text}'")
        print(f"Swapped:  '{swapped_text}'\n")