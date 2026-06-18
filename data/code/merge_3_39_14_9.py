def substring_generator(s: str):
    """
    Generator that yields all possible substrings of a given string.
    
    Args:
        s (str): Input string
        
    Yields:
        str: Substrings starting from index i to j (inclusive) where 0 <= i < len(s) and 0 <= j < len(s)
             Iteration order is by start index, then increasing end indices.
    
    Example output for "abc": 
        'a', 'ab', 'abc'
        'b', 'bc'
        'c'
    """
    length = len(s)
    
    # Iterate through all possible starting positions
    for i in range(length):
        # For each start position, iterate through all ending positions (inclusive of current char)
        for j in range(i + 1):
            yield s[i:j+1]

if __name__ == '__main__':
    sample_string = "abc"
    
    print(f"\nGenerating substrings from '{sample_string}':")
    print("-" * 40)
    
    for substring in substring_generator(sample_string):
        print(substring)