import sys

def swap_adjacent_chars(s: str) -> str:
    """
    Swaps every pair of adjacent characters in a string.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with swapped pairs. If the length is odd, 
             the last character remains unchanged.
    """
    result = []
    i = 0
    
    # Iterate through the string in steps of 2
    while i < len(s):
        if i + 1 < len(s):
            # Swap current and next characters
            pair = s[i] + s[i+1]
            swapped_pair = pair[1] + pair[0]
            result.append(swapped_pair)
            i += 2
        else:
            # Handle odd-length string by keeping the last character as is
            result.append(s[i])
            break
            
    return ''.join(result)

if __name__ == '__main__':
    sample_inputs = [
        "abcdef",
        "aabbccdd",
        "python",
        "",
        "x"
    ]
    
    for test_input in sample_inputs:
        output = swap_adjacent_chars(test_input)
        print(output)