def swap_characters(s: str) -> str:
    """
    Swaps the positions of every adjacent pair of characters in a string.
    
    Args:
        s (str): The input string to modify and return.
        
    Returns:
        str: The modified string with swapped adjacent pairs.
    """
    char_list = list(s)
    n = len(char_list)
    
    # Iterate through the string in steps of 2, swapping characters at indices i and i+1
    for i in range(0, n - 1, 2):
        if i + 1 < n:
            char_list[i], char_list[i + 1] = char_list[i + 1], char_list[i]
            
    return "".join(char_list)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the function runs without user input or external dependencies
    test_cases = [
        "hello",
        "pythonic",
        "abcdefg",
        "",
        "a"
    ]

    for case in test_cases:
        result = swap_characters(case)
        print(f'Original: "{case}" -> Swapped: "{result}"')