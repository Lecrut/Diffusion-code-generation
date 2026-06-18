import sys

def extract_substrings(phrase: str, indices: list[int]) -> None:
    """
    Extracts substrings from a phrase based on provided character indices.
    
    Args:
        phrase (str): The input string to process.
        indices (list of int): A list of integer positions in the string.
        
    Prints each extracted substring separated by newlines or spaces if multiple exist,
    handling out-of-bounds and non-integer inputs gracefully within this function scope.
    
    Note: This function assumes 'indices' is already validated as a list of integers 
    before being passed here to keep the logic focused on extraction.
    """
    results = []
    
    for idx in indices:
        if not isinstance(idx, int):
            # Skip non-integer values silently or log warning depending on strictness;
            # per task "clear error handling", we skip invalid types without crashing.
            continue
        
        try:
            start_idx = max(0, min(len(phrase), idx))  # Clamp to valid range [0, len]
            end_idx = min(len(phrase) + 1, start_idx + 1) if isinstance(idx, int) else len(phrase) + 1
            
            substring_start = phrase[start_idx:]
            
        except Exception:
            continue
        
        results.append(substring_start)

    for i in range(len(results)):
        print(f"Substring at index {indices[i]} (if valid): '{results[i]}'")

def main():
    # Hard-coded sample values as per requirement to avoid input(), sys.stdin, etc.
    phrase = "Hello World!"
    
    # Sample list of indices: 0, 5, 12, -3 (negative index), and a float for testing error handling
    valid_indices_sample = [0, 5, 6]  
    invalid_indices_sample = [-1, 9.8, "a"]  

    print("=== Processing Phrase ===")
    extract_substrings(phrase, valid_indices_sample)

    print("\n=== Handling Invalid Indices (Negative/Float/String) ===")
    # Demonstrate handling of edge cases like negative indices and non-integers
    try:
        for idx in invalid_indices_sample:
            if isinstance(idx, int):
                start = max(0, min(len(phrase), abs(idx))) 
                end = len(phrase) + 1
                substring = phrase[start:end]
                print(f"Index {idx}: '{substring}'")
    except Exception as e:
        print(f"Error occurred during invalid index processing: {e}")

if __name__ == '__main__':
    main()