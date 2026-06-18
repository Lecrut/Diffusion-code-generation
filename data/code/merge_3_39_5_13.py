import sys

def generate_substrings(s):
    """
    Generator function that yields all possible non-empty substrings of a given string s.
    
    Memory-efficient approach: Generates each substring on-the-fly rather than storing 
    the entire list in memory, suitable for very long strings as it processes characters iteratively.
    
    Args:
        s (str): The input string to generate substrings from.
        
    Yields:
        str: Individual substrings starting from index 0 up to length-1 and extending 
             further until the end of the original string for each start position.

    Raises:
        TypeError: If 's' is not a string instance.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    
    # Iterate through all possible starting positions (i) from 0 to len(s)-1
    for i in range(len(s)):
        # Extend the substring by appending characters until the end of s
        yield s[i:]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements; no user input or external dependencies.
    test_string = "ABC"
    
    print(f"Generating substrings for: '{test_string}'")
    
    count = 0
    
    # Process generator directly to yield items one by one (memory efficient)
    try:
        for substring in generate_substrings(test_string):
            count += 1
            print(substring, end=' ')
        
        print()  # Newline after printing all substrings
        print(f"Total number of non-empty substrings generated: {count}")
    except TypeError as e:
        print(f"Error occurred during processing: {e}", file=sys.stderr)