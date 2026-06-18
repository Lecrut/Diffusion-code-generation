def extract_substrings(text: str, indices) -> list[str]:
    """
    Extracts substrings from a given string based on provided start and end index pairs.
    
    Args:
        text (str): The input string to process.
        indices (list[list[int]]): A list of lists where each inner list contains 
                                  two integers [start, end] representing the slice range.
                                  
    Returns:
        list[str]: A list of substrings extracted according to the provided index ranges.
        
    Note:
        - Indices are inclusive for start and exclusive for end (standard Python slicing behavior).
        - If any indices in a pair are out of bounds, they will be clamped to valid ranges 
          within the string length to prevent errors while maintaining robustness.

    Example:
        >>> text = "Hello World"
        >>> extract_substrings(text, [[0, 5], [6, 12]])
        ['Hello', 'World']
    """
    
    # Validate input types early for efficiency and clarity
    if not isinstance(text, str):
        raise TypeError("The first argument must be a string.")
        
    if not isinstance(indices, list) or not all(isinstance(pair, (list, tuple)) 
                                                   and len(pair) == 2 
                                                   and all(isinstance(i, int) for i in pair) 
                                                   for pair in indices):
        raise ValueError("Indices must be a list of pairs containing two integers.")

    result = []
    
    # Pre-calculate string length to avoid repeated lookups during iteration
    text_length = len(text)
    
    for start, end in indices:
        # Clamp the range to valid bounds [0, text_length]
        clamped_start = max(0, min(start, text_length))
        clamped_end = max(clamped_start, min(end, text_length + 1)) if start > end else min(end, text_length)
        
        # Ensure correct handling of reversed or invalid ranges by swapping if necessary and clamping
        actual_start = min(clamped_start, clamped_end)
        actual_end = max(clamped_start, clamped_end)
        
        result.append(text[actual_start:actual_end])

    return result

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    test_string = "Python Programming is Fun!"
    index_pairs = [
        [0, 6],       # 'Python'
        [8, 15],      # 'Program' (note: space at 7) -> actually indices 8 to 14 in string? Let's trace carefully.
                     # String: P(0)y(1)t(2)h(3)o(4)n(5)_(6)p(7)r(8)o(9)g(10)r(11)a(12)m(13)i(14)n(15)...
        [7, 13],      # 'program' (lowercase p at index 7? Wait: "Python _Programming")
                     # Let's re-evaluate indices based on actual string content.
    ]

    # Corrected trace for clarity in sample logic without hardcoding expected output manually to avoid confusion:
    # String: "Python Programming is Fun!" (length 26)
    # Indices [0, 5] -> 'Pytho' ? No, let's use clear ranges.
    
    refined_pairs = [[0, 6], [7, 13]] 
    # [0, 6]: P-y-t-h-o-n (indices 0-5) + _? No: text[0:6] is 'Python' if length matches.
    # Let's just use simple clear ranges for the demo.

    sample_string = "Hello World"
    sample_indices = [[0, 5], [7, 12]] 

    output_list = extract_substrings(sample_string, sample_indices)
    
    print("Input String:", sample_string)
    print("Indices Pairs:", sample_indices)
    print("Extracted Substrings:")
    for i, sub in enumerate(output_list):
        print(f"  [{i}]: '{sub}'")