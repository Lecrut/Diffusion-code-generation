import sys

def swap_adjacent_pairs(s: str) -> str:
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
    
    # Iterate through the string in steps of 2
    while i < len(s):
        if i + 1 < len(s):
            # Swap current character and next one, then append to list
            pair = s[i:i+2]
            result.append(pair[1])
            result.append(pair[0])
            i += 2
        else:
            # Handle the last odd character if any
            result.append(s[i])
            break
            
    return ''.join(result)

if __name__ == '__main__':
    sample_inputs = [
        "abcdef",
        "python",
        "",
        "a"
    ]
    
    for text in sample_inputs:
        output_str = swap_adjacent_pairs(text)
        print(output_str)