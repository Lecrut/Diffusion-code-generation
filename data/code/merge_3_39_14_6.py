import sys

def generate_substrings(s: str):
    """
    Generator that yields all possible substrings of a given string s.
    
    Args:
        s (str): The input string to process.
        
    Yields:
        tuple: A tuple containing the start index, end index, and substring itself.
               This avoids storing full strings in memory unnecessarily until needed.
       
    Example usage example
    
    >>> list(generate_substrings("ABC"))
    [(0, 1, 'A'), (0, 2, 'AB'), (0, 3, 'ABC')]
    
    """

    n = len(s)
    for start in range(n):
        # Optimization: slicing creates a copy; we yield the tuple first.
        # If full substring is needed later without copying at this stage, logic can adjust.
        # However, Python's slice() creates a new string anyway if returned as argument to yield.
        # To be memory efficient here in terms of loop structure: iterate start then end.
        
        for end_index in range(start + 1, n + 1):
            substring = s[start:end_index]
            yield (start, end_index - 1, substring)

if __name__ == '__main__':
    sample_str = "ABC"
    
    # Test the generator function
    results = list(generate_substrings(sample_str))
    
    print(f"Substrings of '{sample_str}':")
    for item in results:
        start, end, sub = item
        print(f"Start {start}, End {end}: '{sub}'")