def extract_substrings(text: str, start_indices: list[int], end_indices: list[int]) -> list[str]:
    """
    Extract all substrings from text where each substring starts at a position in start_indices
    and ends immediately before the corresponding position in end_indices.
    
    Args:
        text (str): The input string to search within.
        start_indices (list of int): List of starting positions for substrings.
        end_indices (list of int): List of ending positions for substrings.
        
    Returns:
        list[str]: A list of extracted substrings in the same order as indices provided.
    
    Raises:
        ValueError: If lists are not of equal length or if any index is out of bounds.
    """
    if len(start_indices) != len(end_indices):
        raise ValueError("start_indices and end_indices must be of equal length.")
    
    for s, e in zip(start_indices, end_indices):
        if not (0 <= s < len(text)) or not (s < e < len(text)):
            raise ValueError(f"Index {s} to {e} is out of bounds or invalid order.")

    return [text[s:e] for s, e in zip(start_indices, end_indices)]

if __name__ == '__main__':
    target_string = "Hello World! Welcome to Python."
    start_points = [0, 6, 13]
    end_points = [5, 12, 19]

    result_substrings = extract_substrings(target_string, start_points, end_points)
    
    print("Extracted substrings:")
    for i, sub in enumerate(result_substrings):
        print(f"Index {i}: '{sub}'")