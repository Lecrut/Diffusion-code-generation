def extract_substrings(text: str, indices) -> list[str]:
    """
    Extracts substrings from a given text based on provided start and end index pairs.
    
    Args:
        text (str): The input string to process.
        indices (list[tuple[int, int]] or list[list[int]]): A flat list of [start, end] 
            tuples/lists representing the boundaries for substring extraction.
            
    Returns:
        list[str]: A list containing the extracted substrings in order.
        
    Note:
        - Indices are inclusive-exclusive (similar to Python slicing).
        - If start >= end or indices contain invalid ranges, empty strings will be returned 
          rather than raising errors for robustness unless specific validation is needed.
        - Time complexity per substring extraction is O(n) where n is the length of text + m*m 
          where m is number of substrings (due to string creation), but slicing in Python is 
          optimized at C level, making this highly efficient for typical use cases.
    """
    # Normalize input: ensure all elements are lists/tuples with exactly two integers
    normalized_indices = []

if __name__ == '__main__':
    pass
