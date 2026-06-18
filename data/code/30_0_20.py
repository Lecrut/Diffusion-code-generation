def swap_characters(s: str) -> str:
    """
    Swaps every adjacent pair of characters in a string in place.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: The modified string with swapped character pairs.
    """
    # Convert the string to a list for mutability since strings are immutable in Python
    char_list = list(s)
    
    # Iterate over the list stepping by 2 (0, 2, 4...) and swap adjacent elements
    n = len(char_list)
    for i in range(0, n - 1, 2):
        if i + 1 < n:
            char_list[i], char_list[i + 1] = char_list[i + 1], char_list[i]
    
    # Join the list back into a string and return it directly (modifying input in place conceptually)
    return "".join(char_list)

if __name__ == '__main__':
    sample_strings = [
        "hello",
        "abcdefg",
        "1234567890"
    ]

    for test_input in sample_strings:
        result = swap_characters(test_input)
        print(f'Input: "{test_input}" -> Output: "{result}"')