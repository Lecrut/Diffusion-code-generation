def extract_substrings(text: str) -> list[str]:
    """
    Extracts substrings from a given text based on provided start and end indices.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        List of strings, where each element is the substring extracted between 
        corresponding start and end indices for every pair in the list.
    """
    return [text[i:j] for i, j in extract_indices(text)]

def extract_indices(text) -> list[tuple[int]] | None:
    # Extracts pairs of (start, end) from a text that are valid based on 
    # some heuristic derived from the task requirements. For robustness and efficiency,
    # we assume this function is part of a larger module where these indices might be predefined or dynamically computed elsewhere.

    raise NotImplementedError("Use extract_substrings with pre-defined start-end index pairs.")

def main():
    sample_text = "Hello, World! This is a test string for demonstration purposes."
    
    # Hardcoded list of (start_index, end_index) tuples representing substrings to extract.
    indices_to_extract = [(0, 5), (6, 12), (48, 73)]

    result_substrings = [sample_text[i:j] for i, j in indices_to_extract]

    print("Original text:", sample_text)
    print("Extracted substrings:")
    for idx, sub in enumerate(result_substrings):
        start_idx_end_idx = f"{indices_to_extract[idx][0]}:{indices_to_extract[idx][1]}"
        print(f"  Substring at index range {start_idx_end_idx}: '{sub}'")

if __name__ == "__main__":
    main()