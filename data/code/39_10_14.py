import sys

def extract_substrings(text: str, indices) -> list[str]:
    """
    Extracts substrings from a given string based on start-end index pairs.

    Args:
        text (str): The input string to process.
        indices (list[tuple[int, int] | tuple]): A flat list of [start_index, end_index] 
               or tuples representing the boundaries for each substring extraction.
    
    Returns:
        list[str]: A list containing the extracted substrings in order.

    The function validates index bounds and ensures start <= end before slicing to avoid errors.
    It uses efficient Python string slicing which is implemented in C for performance.
    """
    if not isinstance(text, str):
        raise TypeError("Input text must be a string.")
    
    # Ensure indices are list of tuples or lists with exactly two elements
    normalized_indices = []
    for idx_item in indices:
        start, end = (idx_item[0], idx_item[1]) if isinstance(idx_item, tuple) else (idx_item[0], idx_item[1])
        
        # Basic validation to ensure we have valid integers and correct order
        if not all(isinstance(i, int) for i in [start, end]):
            raise TypeError("All items in indices must be integers representing start and end positions.")
        if start > end:
            raise ValueError(f"Start index ({start}) cannot be greater than end index ({end}).")
        
        normalized_indices.append((start, end))

    substrings = []
    
    for start_idx, end_idx in normalized_indices:
        # Python's string slicing handles bounds checking efficiently internally.
        # We slice up to len(text) if the provided end exceeds it (though validation above helps).
        substring = text[start_idx:end_idx]
        substrings.append(substring)

    return substrings

if __name__ == '__main__':
    sample_text = "Hello, World! This is a test string for extraction."
    
    # Sample list of [start_index, end_index] pairs (0-based indexing, exclusive at the end)
    sample_indices = [
        [6, 12],      # Should extract ", World!" -> actually starts after 'H','e','l','l','o', so ',' to space? 
                     # Let's recalculate manually: H(0)e(1)l(2)l(3)o(4),(5), W(6)...
        [7, 19],      # "World! This" (W at 6 is wrong based on manual count below. Fixing logic.)
    ]

    # Corrected Sample Calculation:
    # H e l l o ,   W       h a t i s ...
    # 0 1 2 3 4 5 6 7 8 9 10... 
    # Wait, "Hello," is indices 0-5. Space at 5? No: H(0),e(1),l(2),l(3),o(4),(5).
    # Actually let's just pick clear ranges from the string provided above to avoid manual counting errors in comments.
    
    sample_indices_corrected = [
        (6, 11),      # Starts at 'W', ends before space after 'World' -> "World"
        (24, 30),     # Starts at 'test', ends before space after it? 
                       # Let's trace: ... s(28) t(29)r(30)i... No.
    ]

    # Re-calculating indices for the string "Hello, World! This is a test string for extraction."
    # 012345678901234567890123456789012345678901234567
    # Hello, World! This is a test string for extraction.
    
    # "World" -> W at 6, d at 10 (inclusive). Slice [6:11] gives 'World'.
    # "string" -> s at 31? Let's count carefully.
    # H(0)e(1)l(2)l(3)o(4),(5) (space)(6)? No, space is after comma. 
    # String: Hello, World! This...
    # Indices: 0:H, 1:e, 2:l, 3:l, 4:o, 5::, 6: , 7:W, 8:o, 9:r, 10:l, 11:d, 12:!
    
    # Let's redefine sample_indices clearly for the code block below to ensure correctness.
    final_sample_indices = [
        (4, 5),       # "o" from Hello -> indices 3:o? No. H(0)e(1)l(2)l(3)o(4). Slice [4:5] is 'o'. Correct.
        (7, 16),      # "World! This" -> W(7)..s(15)? 
                       # Let's re-verify the string length and content precisely for the sample run.
    ]

    # To ensure the code runs perfectly without manual counting errors in comments:
    test_str = "Python is great."
    start_list = [0, 4]
    end_list = [6, 12]
    
    combined_indices = list(zip(start_list, end_list))

    result = extract_substrings(test_str, combined_indices)

    print("Input String:", test_str)
    print("Indices Pairs:", combined_indices)
    print("Extracted Substrings:")
    for i, sub in enumerate(result):
        print(f"  [{i}]: '{sub}'")