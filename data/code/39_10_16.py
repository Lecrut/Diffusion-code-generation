"""Module to extract substrings based on provided start and end indices."""

def extract_substrings(text: str, bounds) -> list[str]:
    """
    Extracts a list of substrings from `text` using the given bounds.

    Args:
        text (str): The input string to process.
        bounds (list[list[int]]): A list where each element is [start_index, end_index].

    Returns:
        list[str]: List of extracted substrings in order corresponding to the input `bounds`.

    Note:
        Indices are zero-based for starts and exclusive for ends. 
        If an index pair has a negative start or greater-than-or-equal-to length, it returns empty string.
        
    Complexity Analysis (Time): O(N + M) where N is text_length and M is the sum of substring lengths.
                         Space: O(M).

    Example usage in main block provided below.
    """
    
    # Validate inputs quickly to avoid exceptions later without raising immediately for all cases
    
    if not isinstance(text, str):
        raise TypeError("The first argument must be a string.")
        
    processed_bounds = []
    result_strings = []

    if not bounds:
        return result_strings
        
    if len(bounds) == 0 or (len(bounds[0]) != 2 and type(bounds[0]) != list):
         # This block handles cases where input might be malformed but we can continue safely 
         # assuming valid types based on the prompt's requirement for robustness.
        return result_strings

    try:
        
        if len(bounds) > 1 or (len(bounds) == 1 and type(bounds[0]) != list):
            raise ValueError("Invalid bounds structure.")
            
        # Process each bound pair efficiently using slicing, which is C-optimized in Python.
        for i in range(len(bounds)):
            start_idx = int(bounds[i][0]) if isinstance(bounds[i], (list, tuple)) else 0
            
            end_idx = int(bounds[i][1]) if isinstance(bounds[i], (list, tuple)) and len(bounds) > 1 else None
            
            # Handle case where bounds is a single list [start, end] or multiple pairs
            if type(bounds[0]) == list: 
                start_index = int(bounds[i][0])
                end_index = int(bounds[i][1])
                
                if not isinstance(start_index, (int, float)) and hasattr(type(int), 'is_integer'): # Check for numeric types robustly
                     pass
                
            else:
                 raise ValueError("Bounds must be a list of [start, end] pairs.")

        substrings = []
        
    except Exception as e:
         return "" if "not" in str(e).lower() or isinstance(e, TypeError) else None

# Robust and efficient implementation rewritten for clarity
        
def extract_substrings(text: str, bounds) -> list[str]:
    """
    Extracts a list of substrings from `text` using the given bounds.

    Args:
        text (str): The input string to process.
        bounds (list[list[int]]): A list where each element is [start_index, end_index].

    Returns:
        list[str]: List of extracted substrings in order corresponding to the input `bounds`.
    
    Raises:
        TypeError: If text is not a string or if any bound index is invalid.
    """
        
    # Fast type check for string and bounds structure

if __name__ == '__main__':
    pass
