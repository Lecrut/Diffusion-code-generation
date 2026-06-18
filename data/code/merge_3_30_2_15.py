import sys

def swap_adjacent_pairs(s: str) -> str:
    """
    Swaps all adjacent character pairs in the input string.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with every pair of characters swapped.
             If the length is odd, the last character remains unchanged.
    """
    result = []
    i = 0
    
    while i < len(s):
        if i + 1 < len(s):
            # Swap current and next character
            result.append(s[i + 1])
            result.append(s[i])
            i += 2
        else:
            # Handle odd length string by keeping the last char as is
            result.append(s[i])
            break
            
    return ''.join(result)

if __name__ == '__main__':
    sample_input = "abcdef"
    
    output_string = swap_adjacent_pairs(sample_input)
    
    print(output_string)