def extract_substrings(phrase: str, indices: list[int]) -> None:
    """
    Extracts substrings from a phrase based on provided character indices.
    
    Args:
        phrase (str): The input string to process.
        indices (list[int]): A list of integer indices indicating start positions.
        
    Prints each extracted substring separated by newlines or spaces if multiple matches per index? 
    Clarification from task: "prints each extracted substring". Assuming one substring per valid index,
    where the substring starts at that index and extends to the end (or a fixed length?).
    
    Re-reading standard interpretation for such tasks without further spec:
    Usually, it means extracting substrings starting at those indices up to some logical bound.
    However, since no length is specified, we assume extraction from start_index to end of string? 
    Or perhaps just the character itself? The prompt says "substring", implying >1 char possible.
    
    Let's interpret as: for each index i in indices, extract phrase[i:] (from that index to end).
    This allows demonstrating substring behavior clearly.

    Error handling ensures invalid indices raise descriptive exceptions instead of crashing silently or with generic errors.
    """
    if not isinstance(phrase, str):
        raise TypeError(f"Expected 'str' for phrase, got {type(phrase).__name__}")
    
    if not all(isinstance(idx, int) and idx >= 0 for idx in indices):
        invalid_indices = [idx for idx in indices if not (isinstance(idx, int) and idx >= 0)]
        raise ValueError(f"Invalid index values found: {invalid_indices}. Indices must be non-negative integers.")

    substrings = []
    
    # Process each valid start index to extract substring from that point to the end of phrase
    for i in indices:
        if not (i < len(phrase)):
            raise IndexError(f"Index {i} is out of range. Phrase length is {len(phrase)}.")
        
        substrings.append(phrase[i:])

    # Print each extracted substring on a new line as per typical console output expectations for such tasks
    print('\n'.join(substrings))

if __name__ == '__main__':
    phrase = "Hello, World!"
    indices = [0, 5, 7]
    
    try:
        extract_substrings(phrase, indices)
    except (TypeError, ValueError, IndexError) as e:
        print(f"Error occurred during processing: {e}")