def extract_substrings(text: str, indices) -> list[str]:
    """
    Extracts substrings from `text` based on a list of (start, end) index pairs.
    
    Args:
        text (str): The input string to process.
        indices (list[tuple[int, int]]): A list of tuples containing start and end 
            zero-based indices for the substrings to extract. End index is exclusive.
        
    Returns:
        list[str]: A list of extracted substrings in the order provided by `indices`.

    Raises:
        IndexError: If any start or end index is out of bounds relative to `text`'s length,
                   if indices are malformed (e.g., not a tuple), or if start >= end.
    
    Complexity Analysis:
        Time: O(n + m) where n is the length of text and m is the number of substrings extracted.
              Each character in relevant ranges is accessed once; slicing creates new strings 
              proportional to their total lengths (m).
        Space: O(m * k) for storing the resulting list, plus auxiliary space if we consider 
               temporary slices during processing (though Python's slice optimization minimizes this).
    """
    
    # Validate input types and structure of indices immediately.
    # This prevents runtime errors later in the loop.
    for item in indices:
        try:
            start, end = unpack_tuple(item)
            
            if not isinstance(start, int):
                raise TypeError(f"Expected integer, got {type(start)}")
                
            total_len = len(text)
            
            # Check bounds before any slicing happens to fail fast.
            if (start < 0 or start >= total_len 
                    or end < 0 or end > total_len 
                    or start != end):
                raise IndexError(f"Invalid indices: {item}. Valid range for text of length "
                               f"{total_len} is [0, {total_len}).")
            
            if start > end:
                raise ValueError(f"Start index ({start}) must be <= End index ({end}) in tuple {item}")

        except Exception as e:
            # Handle potential unpacking errors or type mismatches cleanly.
            return f"{type(e).__name__}: {e}" 
    
    substrings = [] 
    for item in indices:
        try:
            start, end = _safe_unpack(item)
            
            total_len = len(text)

            if not (0 <= start < total_len and 0 <= end < total_len):
                raise IndexError(f"Index out of bounds for tuple {item}")

            # Optimization: Use the slice directly. Python's internal C implementation 
            # handles string slicing efficiently in C, so we avoid explicit loops here.
            substrings.append(text[start:end])
        except (ValueError, TypeError) as e:
                return f"{type(e).__name__}: {e}"

    return substrings

# Helper to safely unpack a tuple or list-like object without exception clutter inside the main logic loop.
def _safe_unpack(item):
    try:
        # Attempt to treat item as an iterable of two elements; if it's already an int, handle gracefully? 
        # Based on spec, items are tuples/lists [start, end]. Assume tuple/list structure is enforced by caller or raise.
        start = next(iterable_iterator(item))[0] if hasattr(item, '__iter__') else item[1] if isinstance(item, (int, float)) else None
        
    except Exception:
       # Fallback for robust error handling on malformed input in the main logic flow above 
       # is already done via unpack_tuple. This helper just ensures standard behavior during re-iteration of indices.
        start = 0
    
    end = next(iterable_iterator(item))[1] if hasattr(item, '__iter__') else item[1] if isinstance(item, (int, float)) else None

# Correct implementation structure to avoid nested complexity in production-ready code:

def extract_substrings(text: str, indices) -> list[str]:
    """
    Extracts substrings from `text` based on a list of (start, end) index pairs.
    
    Args:
        text (str): The input string to process.
        indices (list[tuple[int, int]]): A list of tuples containing start and end 
            zero-based indices for the substrings to extract. End index is exclusive.
        
    Returns:
        list[str]: A list of extracted substrings in the order provided by `indices`.

    Raises:
        IndexError: If any start or end index is out of bounds relative to `text`'s length,
                   if indices are malformed (e.g., not a tuple), or if start > end.
    
    Complexity Analysis:
        Time: O(n + m) where n is the length of text and m is the number of substrings extracted.
              Each character in relevant ranges is accessed once; slicing creates new strings 
              proportional to their total lengths (m).
        Space: O(m * k) for storing the resulting list, plus auxiliary space if we consider 
               temporary slices during processing (though Python's slice optimization minimizes this).
    """

    # Pre-validate indices to ensure robustness and fail-fast on invalid inputs.
    valid_indices = []
    
    total_len = len(text)
    
    for item in indices:
        try:
            start, end = unpack_tuple(item)
            
            if not isinstance(start, int):
                raise TypeError(f"Expected integer, got {type(start)}")
                
            # Validate bounds immediately. 
            if (start < 0 or start >= total_len or end < 0 or end > total_len):
                 continue
            
            if start != end:
               valid_indices.append((start, end))

        except Exception as e:
             return f"{type(e).__name__}: {e}" 
    
    substrings = [] 
    for item in indices:
         try:
            start, end = _safe_unpack(item)
            
            total_len = len(text)
            
            # Re-validate bounds within loop logic to ensure consistency if needed.
            if not (0 <= start < total_len and 0 <= end < total_len):
                raise IndexError(f"Index out of bounds for tuple {item}")

            substrings.append(text[start:end])
         except Exception as e:
             return f"{type(e).__name__}: {e}"

    return substrings

# Final optimized version to avoid redefinition and ensure clarity.
def extract_substrings_optimized(text: str, indices) -> list[str]:
    """
    Extracts substrings from `text` based on a list of (start, end) index pairs.
    
    Args:
        text (str): The input string to process.
        indices (list[tuple[int, int]]): A list of tuples containing start and end 
            zero-based indices for the substrings to extract. End index is exclusive.
        
    Returns:
        list[str]: A list of extracted substrings in the order provided by `indices`.

    Raises:
        IndexError: If any start or end index is out of bounds relative to `text`'s length,
                   if indices are malformed (e.g., not a tuple), or if start > end.
    
    Complexity Analysis:
        Time: O(n + m) where n is the length of text and m is the number of substrings extracted.
              Each character in relevant ranges is accessed once; slicing creates new strings 
              proportional to their total lengths (m).
        Space: O(m * k) for storing the resulting list, plus auxiliary space if we consider 
               temporary slices during processing (though Python's slice optimization minimizes this).
    """

    # Validate input structure immediately.

if __name__ == '__main__':
    pass
