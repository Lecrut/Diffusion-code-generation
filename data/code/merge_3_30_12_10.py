import sys

def swap_adjacent_chars(s: str) -> str:
    """
    Swaps every pair of adjacent characters in a string.
    
    If the string length is odd, the last character remains unchanged.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with swapped pairs.
    """
    result = []
    i = 0
    
    # Iterate through the string in steps of two
    while i < len(s):
        if i + 1 < len(s):
            # Append the second character, then the first for each pair
            result.append(s[i + 1])
            result.append(s[i])
            i += 2
        else:
            # Handle odd-length string by appending the last character as is
            result.append(s[i])
            break
            
    return ''.join(result)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, command-line arguments, 
    # network access, or pre-existing files are required.
    
    test_cases = [
        "abcdefg",  # Odd length: 'ab'->'ba', 'cd'->'dc', 'ef'->'fe', 'g' stays
        "",         # Empty string
        "a",        # Single character
        "1234567890", # Numeric characters for variety
    ]
    
    output = []
    for test_input in test_cases:
        swapped_output = swap_adjacent_chars(test_input)
        output.append(f"Input: '{test_input}' -> Output: '{swapped_output}'")
        
    print('\n'.join(output))