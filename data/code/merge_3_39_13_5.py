def extract_substrings(target: str, start_indices: list, end_indices: list) -> list[str]:
    """
    Extracts all substrings from a target string that fall between specified 
    non-overlapping start and end point indices (inclusive).
    
    Args:
        target: The input string.
        start_indices: List of starting index positions.
        end_indices: Corresponding list of ending index positions for each start position.
        
    Returns:
        A list of extracted substrings corresponding to the defined ranges.
    """
    if len(start_indices) != len(end_indices):
        raise ValueError("start_indices and end_indices must be of equal length.")

    results = []
    
    # Validate that all indices are within bounds relative to their pair
    for i, (s, e) in enumerate(zip(start_indices, end_indices)):
        if s < 0 or e >= len(target):
            raise IndexError(f"Index {i} falls outside the string boundaries.")
        if s > e:
            continue # Skip invalid ranges where start is after end

    for i, (s, e) in enumerate(zip(start_indices, end_indices)):
        substring = target[s:e+1]  # Slice includes both endpoints
        results.append(substring)

    return results

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    target_text = "Python is powerful and versatile."
    
    # Define start and end indices pairs (inclusive).
    start_points = [0, 6, 12]        # 'P', 'h', 'f' positions
    end_points   = [5, 8, 9]         # 'o', 'w', 'e' positions

    extracted = extract_substrings(target_text, start_points, end_points)

    print("Extracted substrings:")
    for idx, sub in enumerate(extracted):
        print(f"Range {idx}: '{sub}'")