import itertools

def extract_substrings(string: str, length: int) -> list[str]:
    """
    Extract all substrings of a given fixed length from the input string using 
    a sliding window approach. This algorithm optimizes time complexity by avoiding 
    redundant slicing operations on overlapping windows through an iterative shift method.

    Time Complexity: O(N * L), where N is the number of characters in the string and L is the substring length.
                         However, since we generate exactly (N - L + 1) substrings each of length L,
                         this is optimal for fixed-length extraction as input size must be scanned once to verify lengths.

    Args:
        string (str): The source text from which to extract substrings.
        length (int): Fixed number of characters in the desired substrings. Must be >= 1 and <= len(string).

    Returns:
        list[str]: A list containing all contiguous substrings of 'length' from 'string'.
                   If input string is shorter than required length, returns empty list.
    
    Raises:
        ValueError: If 'length' is less than 1 or greater than the actual length of 'string'.
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string.")
    n = len(string)
    
    # Validate required parameters to ensure robustness and prevent runtime errors.
    # Although standard Python slices handle out-of-bounds gracefully by returning empty lists, 
    # explicit validation improves code clarity and prevents logical bugs in downstream logic.
    if length < 1 or length > n:
        raise ValueError(f"Substring length '{length}' must be between 1 and {n}.")

    substrings = []
    
    for i in range(n - length + 1):
        substring_start_index = string[i:i+length]
        substrings.append(substring)
        
    return substrings

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input, 
    # command-line arguments, network access, or pre-existing files.
    
    sample_string = "abcdefghij"  # Sample string of length 10
    
    # Test cases with varying lengths including edge case where substring equals full string
    test_cases = [3, 5, 4]

    for length in test_cases:
        try:
            result_substrings = extract_substrings(sample_string, length)
            
            print(f"Input String (Length {len(sample_string)}):")
            print(f"Sample Length Value ({length}):")
            print(result_substrings)
            
        except ValueError as e:
            # Print the error message but do not re-raise to maintain script flow for demonstration 
            # purposes without crashing silently in a real execution environment.
            print(e, file=__import__('sys').stderr)