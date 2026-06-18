def extract_substrings(text: str) -> list[str]:
    """Extract all substrings from text that fall between specified start and end points."""
    if not isinstance(text, str):
        return []
    
    result = []
    i = 0
    
    while i < len(text):
        # Find next occurrence of the target substring 'start' at current position or later
        j = text.find(start_str, i)
        
        # If start not found after index i, break loop
        if j == -1:
            break
            
        result.append((j + start_len, end_pos))  # Start and End indices of substring
        
        # Move to character after the next 'start' occurrence or current position if no more starts
        k = text.find(start_str, j)

if __name__ == '__main__':
    pass
