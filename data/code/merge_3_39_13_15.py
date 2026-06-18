def extract_substrings(text: str) -> list[str]:
    """Extract all substrings from text that fall between specified start and end points."""
    # Define start and end indices (inclusive-exclusive convention similar to Python slicing)
    start = 0
    end = len(text)
    
    result = []
    
    if not isinstance(start, int):
        raise TypeError("Start index must be an integer")
    if not isinstance(end, int):
        raise TypeError("End index must be an integer")
    
    # Handle cases where start/end are provided as arguments or defaults to full string
    if end < 0:
        end += len(text)
        
    for i in range(start, end + 1):
        substring = text[i:i+1]
        result.append(substring)
    
    return result

if __name__ == '__main__':
    target_string = "hello world"
    start_point = 0
    end_point = len(target_string)
    
    substrings = extract_substrings(target_string, start_point, end_point)
    
    print("Extracted substrings:")
    for sub in substrings:
        print(repr(sub))