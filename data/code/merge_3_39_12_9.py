import sys

def extract_substrings(phrase: str, indices: list[int]) -> None:
    """
    Extracts substrings from a phrase based on provided character indices.
    
    Args:
        phrase (str): The input string to process.
        indices (list[int]): A list of integer indices indicating start positions for extraction.
        
    Prints each extracted substring separated by newlines. Handles invalid indices gracefully 
    without crashing the script, skipping only those that are out of bounds or non-integers if passed incorrectly.
    
    Raises:
        TypeError: If phrase is not a string or indices is not a list of integers.
        ValueError: If any index in the list is negative or greater than or equal to the length of phrase.
    """
    # Validate input types
    if not isinstance(phrase, str):
        raise TypeError(f"Expected 'str' for phrase, got {type(phrase).__name__}")
    
    if not isinstance(indices, list) or not all(isinstance(i, int) for i in indices):
        raise TypeError("Expected a list of integers for indices.")

    # Validate index ranges
    length = len(phrase)
    invalid_indices_found = False
    
    for idx in indices:
        if idx < 0 or idx >= length:
            print(f"Warning: Index {idx} is out of bounds (length={length}). Skipping.", file=sys.stderr)
            invalid_indices_found = True

    # If no valid extraction can be performed due to all errors, we might choose to exit early 
    # but the task implies processing what's possible. Since indices are start points and not ranges,
    # a single index extracts from that point to end or could imply [start:end] where end is implied as length?
    # Re-reading: "extracted substring" with just an index usually means phrase[idx:] (from index to end).
    # However, sometimes it might mean extracting exactly one character. Given typical CLI tasks without range specification,
    # assuming slice [idx:] is safer for 'substring' extraction from a single point. 
    # But often such tasks imply taking the substring starting at that index up to some limit or just char[idx].
    # Let's assume it means extracting the part of string starting at `indices[i]` until end, as no stop index was provided in input list format description.
    
    for idx in indices:
        if 0 <= idx < length:
            substring = phrase[idx:]
            print(substring)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input, command-line arguments, or network access.
    phrase_sample = "Hello World at Python"
    indices_sample = [0, 5, 12]

    try:
        extract_substrings(phrase_sample, indices_sample)
    except (TypeError, ValueError) as e:
        print(f"Error during execution: {e}", file=sys.stderr)