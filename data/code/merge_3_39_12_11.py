def extract_substrings(phrase: str, indices: list[int]) -> None:
    """
    Extracts substrings from a phrase based on provided character indices 
    (0-based) and prints each substring to the console.
    
    Args:
        phrase (str): The input string to process.
        indices (list[int]): A list of integer indices indicating start positions.
        
    Raises:
        ValueError: If any index is out of bounds or non-integer.
        TypeError: If inputs are not a string and list respectively, 
                   though this function assumes correct types per task constraints.
    """
    if not isinstance(phrase, str):
        raise TypeError("The phrase must be a string.")
    
    if not isinstance(indices, list) or not all(isinstance(i, int) for i in indices):
        raise TypeError("Indices must be a list of integers.")

    # Validate each index against the length of the phrase (0-based indexing)
    max_index = len(phrase) - 1
    
    for idx in indices:
        if idx < 0 or idx > max_index:
            raise ValueError(f"Index {idx} is out of bounds. Valid range: [0, {max_index}]")

    # Extract and print substrings starting at each valid index up to the end of the phrase
    for start_idx in indices:
        substring = phrase[start_idx:]
        print(substring)

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements (no user input, args, or network access)
    sample_phrase = "Hello World"
    sample_indices = [0, 5, 6]

    try:
        extract_substrings(sample_phrase, sample_indices)
    except ValueError as ve:
        print(f"[Error]: {ve}")
    except TypeError as te:
        print(f"[Type Error]: {te}")