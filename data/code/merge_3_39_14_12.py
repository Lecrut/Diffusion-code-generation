def generate_substrings(s: str):
    """
    Generator function that yields all possible substrings of a given string s.
    
    Substrings are defined by iterating through all possible start and end indices (inclusive).
    For each pair (start, end), the substring is extracted as s[start:end+1].
    
    This implementation uses memory efficiency by yielding one substring at a time 
    rather than storing them in a list. It avoids unnecessary string concatenation 
    during generation by using Python's built-in slicing which creates new strings only when yielded.

    Args:
        s (str): The input string to generate substrings from.

    Yields:
        str: Each substring corresponding to the range [start, end].
    
    Example Usage:
        >>> list(generate_substrings("abc"))
        ['a', 'ab', 'abc', 'b', 'bc', 'c']
        
        Note: The order is determined by start index increasing from 0 to len(s)-1, 
              and for each start, end index increasing from start to len(s)-1.
    """
    length = len(s)
    
    # Iterate through all possible starting positions
    for i in range(length):
        # For each starting position, iterate through all ending positions (inclusive of current char)
        for j in range(i, length):
            yield s[i:j+1]

if __name__ == '__main__':
    sample_string = "abc"
    
    print(f"Generating substrings from: '{sample_string}'")
    results = list(generate_substrings(sample_string))
    
    # Display the generated substrings in a readable format
    for idx, substring in enumerate(results):
        print(f"{idx + 1}. '{substring}' (length {len(substring)})")