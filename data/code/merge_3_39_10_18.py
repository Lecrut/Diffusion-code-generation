def extract_substrings(text: str, indices) -> list[str]:
    """
    Extracts substrings from a given string based on provided start and end index pairs.
    
    Args:
        text (str): The input string to process.
        indices (list[list[int]] or list[tuple]): A list of [start, end] pairs 
            where each pair defines the inclusive range for substring extraction.
            
    Returns:
        list[str]: A list containing all extracted substrings in order.
        
    Note: This implementation uses Python's optimized C-level string slicing 
    which is highly efficient compared to manual character iteration or regex operations.
    
    Raises:
        ValueError: If indices contains invalid pairs (e.g., non-integers, start > end).
        TypeError: If input types are incorrect.
    """
    if not isinstance(text, str):
        raise TypeError("First argument must be a string.")
    
    if not isinstance(indices, list):
        raise TypeError("Second argument must be a list of index pairs.")

    result = []
    for pair in indices:
        if len(pair) != 2 or not all(isinstance(i, int) for i in pair):
            raise ValueError(f"Each element in indices must be an integer pair [start, end]. Got {pair}")
        
        start_idx, end_idx = pair
        
        # Ensure indices are within bounds to avoid unexpected behavior with negative indexing interpretation

if __name__ == '__main__':
    pass
