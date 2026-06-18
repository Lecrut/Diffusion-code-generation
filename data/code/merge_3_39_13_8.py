def extract_substrings(text: str, start_indices: list[int], end_indices: list[int]) -> list[str]:
    """Extract substrings from text based on provided start and end index lists."""
    if len(start_indices) != len(end_indices):
        raise ValueError("start_indices and end_indices must have the same length.")
    
    # Validate indices are within bounds
    for i, (s, e) in enumerate(zip(start_indices, end_indices)):
        if s < 0 or e >= len(text) or s > e:
            raise IndexError(f"Invalid index range at pair {i}: start={s}, end={e}")

    return [text[s:e] for s, e in zip(start_indices, end_indices)]

if __name__ == '__main__':
    target_string = "Hello, World! This is a test."
    # Define pairs of (start_index, end_index) to extract substrings
    start_points = [0, 7, 13]      # Indices: 'H', ',', 'T'
    end_points   = [6, 12, 19]     # Indices just after: 'e', ' ', '.'

    result_substrings = extract_substrings(target_string, start_points, end_points)

    print("Extracted substrings:")
    for idx, sub in enumerate(result_substrings):
        print(f"Substring {idx + 1}: '{sub}'")