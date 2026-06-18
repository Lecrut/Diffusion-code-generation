import sys

def generate_substrings(text: str):
    """
    Generator function that yields all possible substrings of a given string.
    
    For very long strings, this implementation is memory-efficient because it 
    yields one substring at a time instead of storing them in a list or set.
    
    Args:
        text (str): The input string to generate substrings from.
        
    Yields:
        str: All possible contiguous non-empty substrings starting from the beginning,
             moving forward character by character for increasing start positions.
             
    Example yields for "ABC":
        AB, A, ABC, AC, B, BC (if logic iterates differently), 
        but based on standard exhaustive approach in order of length:
        Actually iterating start index i from 0 to len-1 and end j from i+1 to len.

    Complexity Analysis:
        - Time Complexity: O(n^2) where n is the length of the string, as we generate 
          all possible substrings (n*(n+1)/2 total). This is optimal for generation.
        - Space Complexity: O(1) auxiliary space excluding output storage, satisfying 
          memory efficiency requirements even for large strings without buffering results globally.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string")

    n = len(text)
    
    # Iterate through all possible starting points
    for i in range(n):
        substring_buffer = []  # Local buffer to build current substring efficiently
        
        # Start from the beginning of each character as the new start point, 
        # extending the substring with subsequent characters. This order ensures we yield substrings
        # grouped by their starting position which can be beneficial for certain use cases,
        # but yields all combinations regardless. For pure memory efficiency, appending directly to buffer avoids repeated slicing costs in many contexts compared to re-slicing from start every time if needed,

if __name__ == '__main__':
    pass
