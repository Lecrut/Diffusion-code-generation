import sys

def swap_adjacent_chars(s: str) -> str:
    """
    Swaps every pair of adjacent characters in the input string.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with swapped pairs, or original if length is 0 or 1.
    """
    # Handle edge cases where swapping isn't possible
    n = len(s)
    if n <= 1:
        return s
    
    result_chars = []
    
    # Iterate through the string in steps of 2 to avoid index errors on odd lengths
    for i in range(0, n - 1, 2):
        # Append second character then first character for each pair
        if i + 1 < n:
            result_chars.append(s[i + 1])
            result_chars.append(s[i])
    
    return ''.join(result_chars)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or files.
    test_cases = [
        "abcdef",
        "",
        "a",
        "ab",
        "python",
        "12345"
    ]
    
    for test_input in test_cases:
        output = swap_adjacent_chars(test_input)
        print(output)