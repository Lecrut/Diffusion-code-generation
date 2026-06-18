def extract_substrings(text: str, indices) -> list[str]:
    """
    Extracts substrings from a given text based on provided start and end index lists.
    
    Args:
        text (str): The input string to process.
        indices (list[list[int]]): A list of pairs where each pair contains [start, end] indices.
                                   Indices are 0-based; the substring includes characters from 
                                   start up to but not including end.
    
    Returns:
        list[str]: A list of extracted substrings corresponding to each index pair in order.
    
    Note:
        This implementation assumes valid input where all pairs have two integers and indices 
        are within bounds relative to the length of text. No error handling for invalid inputs is included 
        per the requirement for a robust function focusing on efficiency, though basic type checking could be added 
        if strict validation were required by specific use cases not mentioned here.
    
    Time Complexity: O(n + m) where n is the length of text and m is the number of index pairs.
    Space Complexity: O(k * avg_len) where k is the number of substrings extracted and avg_len is their average length.
    """
    return [text[i[0]:i[1]] for i in indices]

if __name__ == '__main__':
    sample_text = "Hello, World! This is a test string."
    sample_indices = [[4, 9], [7, 12], [35, 38], [60, 64]]

    result_substrings = extract_substrings(sample_text, sample_indices)

    print("Original Text:", sample_text)
    print("Index Pairs:", sample_indices)
    print("Extracted Substrings:")
    for idx, sub in enumerate(result_substrings):
        print(f"  {idx + 1}. '{sub}'")