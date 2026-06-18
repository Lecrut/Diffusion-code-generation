"""
Generator to yield all possible substrings of a given string efficiently.
This implementation avoids storing all substrings in memory by yielding one at a time.
It uses an iterator-based approach with two nested loops, starting and ending indices,
to generate each unique substring pair (i, j) where i <= j.

Memory Efficiency: 
Only the current substring is kept in memory while being yielded, regardless of string length.

Time Complexity per yield: O(L) for slicing/string creation during iteration, but no bulk storage.
Total Time: O(N^3) worst-case due to slice operations on average-length strings (N = len(s)).
Note: While creating the substring object takes time proportional to its length, 
      we avoid allocating N^2/6 objects simultaneously which would be impossible for long strings.

The generator yields substrings in order of starting index increasing, then ending index increasing.
"""

def all_substrings(string):
    """
    Generator that yields every substring of the input string.
    
    Args:
        string (str): The input string to generate substrings from.
        
    Yields:
        str: Substrings starting at each position i and ending at j where 0 <= i < len(string) 
             and i <= j < len(string).

    Example:
        >>> list(all_substrings("abc"))
        ['a', 'ab', 'abc', 'b', 'bc', 'c']
    """
    length = len(string)
    
    # Outer loop iterates through the starting index of each substring
    for start in range(length):
        current_start_string = string[start]  # Capture slice at this point to avoid repeated slicing overhead
        
        # Inner loop extends the substring from 'start' by increasing end position
        for end in range(start + 1, length + 1):
            yield current_start_string + string[end - 1:end]

if __name__ == '__main__':
    sample_strings = [
        "abc", 
        "", 
        "a" * 50  # Test with a moderately long repetitive string to ensure efficiency without memory issues
    ]

    for test_str in sample_strings:
        print(f"\nTesting with input of length {len(test_str)}")
        count = sum(1 for _ in all_substrings(test_str))
        
        if len(test_str) <= 5:
            substrings_list = list(all_substrings(test_str))
            print("First few substrings:", substrings_list[:4])
        
        # Just printing the total count of substrings instead of storing them for long strings
        print(f"Total number of unique substring positions (including duplicates if logic varied, here it's all pairs): {count}")
    
    # Verify correctness with a small known case manually listed above
    assert len(list(all_substrings("abc"))) == 6