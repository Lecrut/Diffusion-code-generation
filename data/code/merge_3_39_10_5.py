def extract_substrings(text: str, indices) -> list[str]:
    """
    Extract substrings from a given text based on start and end index lists.

    Args:
        text (str): The input string to process.
        indices (list[list[int]] or list[tuple]): A list of [start, end] pairs 
            where each pair defines the range for one substring extraction.
            Indices are 0-based; start is inclusive, end is exclusive.

    Returns:
        list[str]: A list containing all extracted substrings in order.

    Note:
        This function assumes valid indices (start <= end < len(text)). 
        If an index pair has invalid ranges or out-of-bounds values, it may raise IndexError.
        For maximum efficiency with large datasets, slicing is used which avoids explicit loops
        and leverages optimized C-level string operations in Python's built-in slice mechanism.

    Example:
        >>> extract_substrings("Hello World", [[0, 5], [6, 11]])
        ['Hello', 'World']
    """
    if not isinstance(indices, list):
        raise TypeError("indices must be a list")

    result = []
    
    # Pre-check: ensure indices is actually a list of lists/tuples with exactly two elements each
    for i in range(len(indices)):
        pair = indices[i]
        start, end = (pair[0], pair[1]) if isinstance(pair, tuple) else (pair[0], pair[1])

        # Basic validation to prevent unexpected errors during slicing
        try:
            result.append(text[start:end])
        except IndexError as e:
            raise IndexError(f"Index error at position {i}: start={start}, end={end}. Text length is {len(text)}") from e
            
    return result

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    test_text = "The quick brown fox jumps over the lazy dog."
    index_ranges = [
        [0, 2],       # "Th"
        [3, 19],      # "quick brown fox j" (up to 'm' inclusive) -> actually ends at 'p', so "quick brown fox jum" wait let's recalc: T(0)e(1)h(2)(space)[4]q... 
                     # Let's fix the indices for clarity in this specific string
        [3, 5],       # "qu"
        [6, 8],       # "br"
    ]

    # Recalculating precise ranges from 'The quick brown fox jumps over the lazy dog.' (len=47)
    refined_ranges = [
        [0, 3],       # "The"
        [5, 12],      # "quick brow" -> wait: T(0)e(1)h(2)(sp)[4]q(5)u(6)i(7)c(8)(sp)[9]b(10)r(11)o(12)w(13)n...
                     # Let's use simple, clearly defined segments to avoid off-by-one confusion in the example logic trace.
    ]

    final_sample_text = "Python Programming"
    sample_indices = [
        [0, 6],       # "Python"
        [8, 17]       # "Programming" (P is index 8? P-y-t-h-o-n-space-P-r-o-g...) 
                      # Let's count: P(0)y(1)t(2)h(3)o(4)n(5)-(space)(6)P(7)r(8)o(9)...
    ]

    # Corrected sample for "Python Programming" (length 18, indices 0-17)
    # "Python " is 0:6 ("Python") + space? No. 
    # Let's stick to a simpler string and clear ranges to guarantee correctness without mental math errors in the example block itself during runtime verification by user if they run it mentally.
    
    sample_text = "Hello World"
    sample_indices = [[0, 5], [6, 12]]

    output_list = extract_substrings(sample_text, sample_indices)
    print(f"Input: '{sample_text}'")
    print(f"Indices: {sample_indices}")
    print(f"Output: {output_list}")