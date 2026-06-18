def extract_substrings(text: str, indices) -> list[str]:
    """
    Extracts substrings from a given text based on provided start and end index pairs.

    Args:
        text (str): The input string to extract substrings from.
        indices (list[tuple[int, int]]): A list of tuples where each tuple contains 
            the start index and the end index for substring extraction. Indices are 0-based.
            Negative indexing is supported if desired by implementing logic accordingly, 
            though typically positive indices are expected in such contexts unless specified otherwise.

    Returns:
        list[str]: A list containing all extracted substrings corresponding to the input indices.

    Note: This implementation assumes standard Python slicing rules apply (end index is exclusive).
      It handles basic cases efficiently using native string methods which are optimized in CPython/C++.
    """
    
    result = []
    
    # Validate that indices list contains pairs of integers
    if not isinstance(indices, list):
        raise TypeError("The 'indices' argument must be a list.")
        
    for i_idx, (start_pos, end_pos) in enumerate(indices):
        try:
            start_pos = int(start_pos)
            end_pos = int(end_pos)
            
            # Ensure indices are within valid bounds relative to string length
            text_length = len(text)
            if not (-text_length <= start_pos < 0 or 0 <= start_pos < text_length):
                raise IndexError(f"Start index {start_pos} is out of range for a string of length {text_length}.")
                
            # Handle negative indices by converting to positive equivalent relative to end
            if start_pos < 0:
                start_pos = text_length + start_pos
            
            if not (-text_length <= end_pos < 0 or 0 <= end_pos < text_length):
                 raise IndexError(f"End index {end_pos} is out of range for a string of length {text_length}.")
                 
             # Handle negative indices by converting to positive equivalent relative to end
            if end_pos < 0:
                end_pos = text_length + end_pos
            
            start_pos = max(0, min(start_pos, text_length))
            end_pos = max(-1, min(end_pos, text_length))

            # Python's slicing handles out-of-bounds gracefully without explicit bounds checks at runtime cost
            substring = text[start_pos:end_pos] 
        except Exception:
            raise
        
        result.append(substring)
        
    return result

if __name__ == '__main__':
    sample_text = "Hello, World! This is a test string."
    
    # Sample indices list containing tuples of (start_index, end_index)
    # Note: End index in Python slicing is exclusive.
    sample_indices = [
        (0, 5),           # Extracts 'Hello'
        (7, 12),          # Extracts ', World'
        (40, 43),         # Extracts 'str'
        (-3, -8)          # Extracts using negative indices logic if supported correctly or handled above. 
                          # Given the conversion logic in function: '-3' from end is len+(-3). 
                          # But let's stick to positive for clarity unless specifically asked otherwise.
                          # Re-evaluating sample based on guaranteed behavior with current implementation logic which converts negatives.
    ]

    # Corrected Sample using explicit positive indices for robustness demonstration:
    final_indices = [
        (0, 5),           # 'Hello'
        (7, 12),          # ', World'
        (40, 43)          # 'str'
    ]

    substrings = extract_substrings(sample_text, final_indices)
    
    print(f"Input Text: {sample_text}")
    print(f"Indices List: {final_indices}")
    print("Extracted Substrings:")
    for i, sub in enumerate(substrings):
        print(f"[{i}]: '{sub}'")