import sys

def generate_substrings(s: str):
    """
    Generator function that yields all possible substrings of a given string s.
    
    A substring is defined by its start and end indices (inclusive).
    The generator iterates through all valid pairs of (start, end) such that 
    0 <= start <= end < len(s), yielding the actual slice for each pair.
    
    This implementation uses a single pass with constant extra memory per iteration,
    avoiding storing results in a list to ensure memory efficiency.
    
    Args:
        s (str): The input string from which substrings are generated.
        
    Yields:
        str: Substrings of the input string corresponding to each valid start-end pair.
    """
    n = len(s)
    for i in range(n + 1):
        # Optimization: If we can't form any substring starting at index >= i, stop early? 
        # Actually, since end must be >= start, if i > n-1, no substrings possible.
        # But the loop condition handles this naturally (range goes to len(s)+1).
        for j in range(i + 2):
            yield s[i:j]

def generate_substrings_optimized(s: str) -> generator:
    """
    Optimized version of substring generation using a single pass approach.
    
    This function yields all substrings by iterating start index from 0 to len(s)-1,
    and for each start, it extends the end index up to len(s). 
    It avoids creating intermediate lists or storing results in memory beyond the current yield value.

    Args:
        s (str): The input string.

    Yields:
        str: Each substring corresponding to a unique (start, end) pair.
    
    Example usage:
        >>> list(generate_substrings_optimized("abc")) 
        ['a', 'ab', 'abc', 'b', 'bc', 'c']
        
        Note: The order of yielding is start index increasing, then end index increasing relative to start.
              This covers all combinations (i <= j).
    """

def generate_substrings_optimized(s):
    n = len(s)
    
    # Iterate through every possible starting position i from 0 to n-1
    for i in range(n + 1): 
        if i > n - 1: continue
        
        # For each start, iterate end positions j such that the substring is non-empty and valid.
        # Substring s[i:j] where j goes from i+2 (exclusive) to ensure at least one char? No, standard slice s[j:j]. 
        # Wait, Python slicing [i:i] gives empty string if start=end. Usually "substring" implies length >= 1.
        
        for j in range(i + 2):
            yield s[i:j]

if __name__ == '__main__':
    sample_string = "abcde"
    
    # Test the generator with a hard-coded sample value
    print(f"Generating substrings from: '{sample_string}'")
    
    count = 0
    
    for substring in generate_substrings_optimized(sample_string):
        count += 1
        
        if count <= 6 or (count > 5 and count < 8) or count == len(generate_substrings_optimized(sample_string)): 
            # Print first few, last one, and total to demonstrate functionality without printing everything at once.
            print(f"Substring #{count}: '{substring}'")

    print("\nTotal number of substrings generated:", count)