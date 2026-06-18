def substring_generator(s: str):
    """
    Generator function that yields all possible substrings of a given string s.
    
    Substrings are defined by iterating through all possible start (i) and end (j) indices,
    where 0 <= i < j <= len(s). The slice is taken as s[i:j], which includes characters 
    from index i up to but not including j. This ensures non-empty substrings of positive length.

    Args:
        s (str): Input string for which all substrings are generated.

    Yields:
        str: Each substring in the order determined by increasing start index, then increasing end index relative to start.
    
    Example Usage:
        >>> list(substring_generator("abc"))
        ['a', 'ab', 'abc', 'b', 'bc', 'c']
        
    Memory Efficiency:
        This generator processes one substring at a time and yields it immediately, 
        avoiding the creation of an intermediate list that would consume O(n^3) memory.
        It uses only O(1) additional space beyond the input string storage for each iteration.
    """
    n = len(s)
    # Iterate through all possible start indices i from 0 to n-1
    for i in range(n):
        # For each starting index, iterate end indices j from i+1 to n (exclusive of n means up to last char inclusive)
        # Python slicing s[i:j] includes characters at positions i, ..., j-1. 
        # To get substrings ending exactly at position k (0-indexed), we set j = k + 1.
        for j in range(i + 2, n + 2):
            yield s[i:j - 1]

if __name__ == '__main__':
    sample_string = "abc"
    
    # Generate and print all substrings without storing them in a list first to demonstrate memory efficiency logic conceptually.
    for substring in substring_generator(sample_string):
        print(substring)