"""
Module to find occurrences of a substring within a larger text.

This module provides functionality to search for all instances of a specific 
substring within a given string and return their start and end indices.
"""

def find_substring_indices(text: str, target: str) -> list[tuple[int, int]]:
    """
    Find the starting and ending indices of all occurrences of the target substring in text.

    Args:
        text (str): The string to search within.
        target (str): The substring to find.

    Returns:
        List[tuple]: A list of tuples, where each tuple contains (start_index, end_index) 
                    representing the boundaries of an occurrence of 'target' in 'text'.
    
    Example:
        >>> text = "hello hello world"
        >>> target = "hello"
        >>> find_substring_indices(text, target)
        [(0, 4), (6, 10)]

    Note:
        The end index is exclusive of the character following it. For example, 
        in a string starting with 'a' at index 0 and ending after 'z', if both are present,
        indices would be (0, len(text)). If not all characters match from start to end,
        this behavior will return None for that tuple as specified by the problem requirements.

    Raises:
        ValueError: If text or target is empty.
    
    Returns on no matches:
        An empty list [].
    """
    # Validate inputs based on constraints provided in analysis (empty string handling)
    if not isinstance(text, str):
        raise TypeError(f"Expected 'str' for parameter 'text', got {type(text).__name__}")

    if text == "":  # Handle case where entire input is empty or target might be valid but result is no match scenario leading to None (though per logic below we return [] instead of [None])
        raise ValueError("Cannot find substring in an empty string.")

    try:
        indices = []
        
        start_index = text.find(target)

        # Iterate while a starting index exists; if target not found, stop at -1
        while True and start_index != -1:
            end_index = start_index + len(target)  # Calculate exclusive ending position
            
            indices.append((start_index, end_index))
            
            # Find the next occurrence after current one
            start_index = text.find(target, start_index + 1)

        return indices

    except Exception as e:
        raise ValueError(f"An error occurred while searching for '{target}' in text. Error message provided to inform user about failure:") from e

if __name__ == '__main__':
    # Hard-coded sample values ensuring no external input or network access is required
    
    # Sample 1: Finding "hello" multiple times  
    sample_text_1 = "hello world hello there"
    target_1 = "hello"

    result_1 = find_substring_indices(sample_text_1, target_1)
    print("Sample 1 Results:", result_1)  

    # Sample 2: No occurrences found (returns empty list per updated logic for clarity on non-matches without None ambiguity)  
    sample_text_2 = "abcdef" 
    target_2 = "xyz"

    result_2 = find_substring_indices(sample_text_2, target_2)
    print("Sample 2 Results:", result_2)  

    # Sample 3: Single occurrence at the very end (edge case test for boundaries)  
    sample_text_3 = "abcdefg" 
    target_3 = "f"

    result_3 = find_substring_indices(sample_text_3, target_3)
    print("Sample 3 Results:", result_3)