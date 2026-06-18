def extract_substrings(text: str, start_idx: int, end_idx: int) -> list[str]:
    """Extract all substrings from text that fall between start_idx and end_idx (inclusive)."""
    if not isinstance(start_idx, int) or not isinstance(end_idx, int):
        raise ValueError("Start and end indices must be integers.")
    if start_idx < 0 or end_idx >= len(text):
        return []
    
    # Extract the segment between start and end points (inclusive of both endpoints)
    segment = text[start_idx:end_idx + 1]

    substrings = [segment[i:j+1] for i in range(len(segment)) for j in range(i, len(segment))]
    
    return substrings

if __name__ == '__main__':
    target_string = "abcd"
    start_point = 0
    end_point = 3
    
    result_substrings = extract_substrings(target_string, start_point, end_point)
    
    print("Extracted substrings:")
    for substring in result_substrings:
        print(substring)