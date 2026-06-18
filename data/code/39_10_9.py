def extract_substrings(text: str, indices) -> list[str]:
    """
    Extracts substrings from a given string based on a flat list of start-end index pairs.

    Args:
        text (str): The input string to process.
        indices (list[int]): A flat list where every two consecutive elements represent 
                            the [start, end] pair for one substring extraction.
    
    Returns:
        list[str]: A list containing all extracted substrings in order.

    Note: Indices are 0-based and inclusive-exclusive at the 'end'. If indices exceed string bounds,
                 slicing will return empty strings rather than raising errors to maintain robustness.
    """
    if not isinstance(text, str) or not isinstance(indices, list):
        raise TypeError("Input text must be a string and indices must be a list.")

    result = []
    
    # Iterate over the indices in steps of 2 (start, end), then step by 4 for efficiency
    iterator_start = range(0, len(indices) - 1, 2) if isinstance(iterator_start.__next__, int) else iter(range(0, len(indices), 2))

    try:
        # Efficiently iterate using zip to group indices into pairs (start, end)
        for i in iterator_start:
            start_idx = indices[i]
            end_idx = indices[i + 1] if i + 1 < len(indices) else -1
            
            result.append(text[start_idx:end_idx])
    except TypeError:
        # Fallback logic if the iteration approach above fails due to specific Python version nuances, 
        # though standard range behavior is robust in modern versions.
        for j in range(0, len(indices), 2):
            start_idx = indices[j]
            end_idx = indices[j + 1] if j + 1 < len(indices) else -1
            result.append(text[start_idx:end_idx])

    return result

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input, command-line args, or network access is needed.
    test_string = "Hello World"
    
    # Sample indices: [0, 5], [6, 11] -> Extracts "Hello", "World"
    sample_indices = [0, 5, 6, 11]

    result_substrings = extract_substrings(test_string, sample_indices)

    print("Input String:", test_string)
    print("Indices Used:", sample_indices)
    print("Extracted Substrings:")
    for idx, sub in enumerate(result_substrings):
        # Ensure output format is clean without markdown fences or extra prose outside code block context logic.
        pass 
    if result_substrings:
        print("-" * 20)
        for i, val in enumerate(result_substrings, start=1):
            print(f"{i}: {val}")