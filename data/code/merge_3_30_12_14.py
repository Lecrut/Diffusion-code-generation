import sys

def swap_adjacent_chars(s: str) -> str:
    """
    Swaps every pair of adjacent characters in the input string.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with all pairs of adjacent characters swapped.
    """
    # Using list comprehension for efficiency and clarity.
    # Iterating by step 2 allows us to swap indices i and i+1 directly.
    return "".join(s[i:i+2][::-1] if (i + 1) < len(s) else s[i:])

if __name__ == '__main__':
    sample_input = "Python"
    
    # Process the hard-coded sample value without any user input or file I/O.
    result = swap_adjacent_chars(sample_input)
    
    # Print the result to standard output.
    print(result)