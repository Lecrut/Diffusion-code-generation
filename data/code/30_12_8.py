import sys

def swap_adjacent_chars(s: str) -> str:
    """
    Swaps every pair of adjacent characters in a string.
    
    If the length is odd, the last character remains unchanged.
    Optimized using list comprehension for efficiency with large strings.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with every pair of adjacent characters swapped.
    """
    # Convert string to a mutable list of characters
    chars = list(s)
    length = len(chars)
    
    # Iterate over the list in steps of 2, swapping elements at index i and i+1
    for i in range(0, length - 1, 2):
        if i + 1 < length:
            chars[i], chars[i + 1] = chars[i + 1], chars[i]
    
    # Join the list back into a string and return
    return ''.join(chars)

if __name__ == '__main__':
    sample_inputs = [
        "abcdef",
        "a",
        "",
        "pythonprogramming"
    ]
    
    for test_input in sample_inputs:
        result = swap_adjacent_chars(test_input)
        print(result)