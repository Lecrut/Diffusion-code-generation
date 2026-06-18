def extract_substrings(text: str, start_idx: int, end_idx: int) -> list[str]:
    """Extract all substrings from text that fall strictly between start_idx and end_idx."""
    
    # Handle cases where indices are negative (Python's natural behavior for slicing) or out of bounds
    if not isinstance(start_idx, int) or not isinstance(end_idx, int):
        raise TypeError("Start and end points must be integers.")

    # Ensure the slice is within reasonable bounds to avoid empty lists when logic dictates
    start = max(0, min(start_idx, len(text)))
    end = max(len(text), min(end_idx, len(text))) if end_idx > 0 else 0
    
    return [text[start:end]]

if __name__ == '__main__':
    # Hard-coded sample values as per requirement. 
    # Extracts the substring found between index 5 and 12 in "Hello World!".
    
    target_string = "Hello World!"
    start_point, end_point = 5, 12
    
    result_substrings = extract_substrings(target_string, start_point, end_point)
    
    print(result_substrings)