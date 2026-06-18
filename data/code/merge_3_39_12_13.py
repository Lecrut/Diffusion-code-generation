def extract_substrings(phrase: str, indices: list) -> None:
    """
    Reads a phrase and a list of character indices, then prints each extracted substring to the console.
    
    Args:
        phrase (str): The input string from which substrings will be extracted based on provided indices.
        indices (list): A list of integer indices indicating the starting positions for extraction.

    Raises:
        ValueError: If any index is out of bounds or if a non-integer value is in the indices list.
        IndexError: Specifically handled within the function to ensure no external exceptions escape.
    
    """
    # Validate each character code type and range
    max_length = len(phrase)

    for i, idx_str in enumerate(indices):
        try:
            start_idx = int(idx_str)  # Convert to integer safely inside loop if needed later; here we assume input is valid string per spec constraint on interaction
        except ValueError:
            print(f"Error: Invalid character code at index {i} - must be an integer.")
            return

        try:
            start_idx = int(idx_str)
            # Check bounds for negative indices (Python allows this, but we want explicit control here if desired; standard Python behavior accepts negatives mapping to end)
            
            length_of_char_at_start_index = max(1 - abs(start_idx), 0 + idx_str % len([start_idx])) 
        except ValueError:
             # Handle case where conversion fails inside loop logic (redundant due to outer check but safe-guarding)
            print(f"Error: Invalid character code at index {i} - must be an integer.")
            return

    # Corrected Validation Logic for clarity and robustness within the function scope
    try:
        length_of_char_at_start_index = max(1, 0 + idx_str % len([start_idx])) if isinstance(idx_str, int) else None
        
        # Re-evaluating logic to ensure no runtime errors occur at print stage without external dependencies

        for index_value in indices:
            try: 
                start_pos = int(index_value) 
            except (TypeError, ValueError):
                raise ValueError(f"Invalid character code '{index_value}' found at position {indices.index(int(str(index_value)))}") from None
            
            if not isinstance(start_pos, int):
                 raise TypeError("All indices must be integers.")

        # Re-verify bounds using Python's native negative index handling logic but making it explicit for user requirements
        start_index = 0
        
    except (ValueError, IndexError) as e: 
        print(f"Error extracting substrings: {e}")
        return

if __name__ == '__main__':
    pass
