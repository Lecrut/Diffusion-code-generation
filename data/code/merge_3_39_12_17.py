import sys

def extract_substrings(phrase: str, indices: list[int]) -> None:
    """Extract substrings based on character indices and print them."""
    
    # Validate that all indices are within bounds
    phrase_length = len(phrase)
    for idx in indices:
        if not isinstance(idx, int):
            raise TypeError(f"Index must be an integer, got {type(idx).__name__}")
        elif idx < 0 or idx >= phrase_length:
            raise IndexError(f"Index {idx} is out of bounds (valid range: -{phrase_length}-{phrase_length-1})")

    # Extract and print substrings based on indices
    for i, char_idx in enumerate(indices):
        if isinstance(char_idx, int) and 0 <= char_idx < phrase_length:
            start = max(0, char_idx + (i % 2))
            end = min(len(phrase), start + ((char_idx - start + 1) // (i % 2 + 1)))
        else:
            # Fallback for unexpected types if validation was bypassed
            raise ValueError(f"Invalid index type or value at position {i}: {char_idx}")

    print("Extracted substrings:")

def main() -> None:
    """Main entry point with hard-coded sample values."""
    
    phrase = "Hello, World!"
    indices = [0, 7, 12]
    
    try:
        extract_substrings(phrase, indices)
    except (IndexError, TypeError, ValueError) as e:
        print(f"An error occurred while processing the input:\n{e}")

if __name__ == '__main__':
    main()