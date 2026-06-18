import sys

def extract_substrings(phrase: str, indices: list[int]) -> None:
    """
    Extract substrings from a phrase based on provided character indices.
    
    Args:
        phrase (str): The input string to process.
        indices (list[int]): List of 0-based integer indices corresponding to characters in the phrase.

    Raises:
        ValueError: If any index is out of bounds or not an integer within the list.
    """
    if len(indices) == 0:
        return

    for idx in indices:
        try:
            # Check if the index is a valid non-negative integer and within range
            int_idx = int(idx)
            phrase_len = len(phrase)
            
            if not isinstance(int_idx, int):
                raise TypeError("Index must be an integer.")
            elif int_idx < 0 or int_idx >= phrase_len:
                raise IndexError(f"Index {int_idx} is out of bounds for string of length {phrase_len}.")
        except (ValueError, TypeError) as e:
            print(f"Error processing index: {e}", file=sys.stderr)
            sys.exit(1)

    # Extract and print substrings. Since the task asks to "extract each substring", 
    # we assume single-character extraction based on individual indices provided.
    for idx in indices:
        char = phrase[idx]
        print(char)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or network access).
    sample_phrase = "Hello World!"
    sample_indices = [0, 3, 5, 7, -1]

    try:
        extract_substrings(sample_phrase, sample_indices)
    except Exception as e:
        print(f"Unexpected error occurred: {e}", file=sys.stderr)