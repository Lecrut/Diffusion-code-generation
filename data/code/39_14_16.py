"""
Generator function to yield all possible substrings of a given string.
This implementation is optimized for memory efficiency by yielding strings one at a time,
rather than collecting them into a list first.

The generator iterates through every possible start index and end index pair (inclusive).
For each valid substring, it yields the resulting string slice immediately without storing all results in memory.
"""

def generate_substrings(s: str):
    """
    Yields all substrings of the input string s by iterating over all possible 
    combinations of start and stop indices.

    Args:
        s (str): The input string to process.

    Yields:
        str: Substring corresponding to index range [start, end). Note that this logic mirrors slicing behavior where 'end' is exclusive for the slice operation but inclusive in typical substring definition descriptions like "substring from i to j". 
             However, standard Python slicing s[i:j] includes characters at indices i up to (but not including) j.
             To ensure we cover every contiguous sequence of characters exactly once and avoid ambiguity with open/closed intervals:
             We iterate start from 0 to len(s)-1.
             We iterate end from start+1 to len(s)+1, but using exclusive stop indices for slicing yields the full set of non-empty substrings s[start:end] without duplicates due to overlapping definitions if we strictly follow contiguous blocks.

       Actually, let's refine: 
       A substring is defined by two characters (or boundaries).
       Standard interpretation: "substring from index i to j" usually implies inclusive [i, j].
       In Python slicing `s[i:j]` corresponds to indices i <= k < j.
       To generate all contiguous segments of length 1 up to N without duplicates in the set of resulting strings (though duplicate content is allowed if chars repeat), we iterate:
       start_index from 0 to len(s)-1
       end_index_from_start from 0 to len(s) - 1 
       
       The slice s[start : start + length] covers all substrings.

    Example for "ABC":
        Start 0, Len 1 -> 'A' (s[0:1])
        Start 0, Len 2 -> 'AB' (s[0:2])
        Start 0, Len 3 -> 'ABC' (s[0:3])
        ... and so on.

    """
    length = len(s)
    
    # Iterate over all possible start positions from the beginning to the end of the string
    for i in range(length):
        # Determine maximum length starting at this position
        max_len = length - i
        
        # Yield substrings with lengths 1 up to max_len, slicing ensures we get unique contiguous segments per start point
        for j in range(1, max_len + 1):
            yield s[i : i + j]

if __name__ == '__main__':
    sample_string = "ABC"

    print(f"The input string is: {sample_string}")
    
    # Calculate total count first to show efficiency (without storing in memory)
    substring_count = sum(1 for _ in generate_substrings(sample_string))
    print("Total number of possible substrings:", substring_count)
    
    print("\nList of all substrings generated:")
    results_list = []
    # Collect them here just to display, the generator itself only holds one state at a time. 
    # In production with large strings (millions/chars), do not store in list; process directly if needed.
    
    for sub_string in generate_substrings(sample_string):
        results_list.append(sub_string)
        
    print(results_list)

    print("\nDemonstrating direct usage without storage:")
    # Re-run generator to demonstrate true lazy evaluation behavior conceptually
    count = 0
    found_none = True
    for sub in generate_substrings(sample_string):
        count += 1
        if len(sub) == 3: 
            print(f"Full string substring found at iteration {count}: '{sub}'")
        
        # Logic check to ensure loop finishes (simulated break condition not needed as generator yields all)
    print("Direct generation completed successfully.")