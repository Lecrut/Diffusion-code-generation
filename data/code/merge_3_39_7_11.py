"""
Algorithm to extract all substrings of length L from string S using sliding window technique.
Time Complexity: O((N - L + 1) * L), where N is the length of string S and L is substring length.
Space Complexity: O(1) auxiliary (excluding output storage).

The algorithm uses a fixed-size window that slides one character at a time across the input string,
extracting substrings efficiently without re-scanning characters unnecessarily for each step once the initial window is formed.
"""

def extract_substrings(string_s: str, length_l: int) -> list[str]:
    """
    Extract all contiguous substrings of specified length from the given string.

    Args:
        string_s (str): The input source string.
        length_l (int): The desired length for each substring. Must be positive and not exceed len(string_s).

    Returns:
        list[str]: A list containing all valid substrings of length L extracted from S.

    Raises:
        ValueError: If length is non-positive or greater than the string length.
    """
    if length_l <= 0:
        raise ValueError("Length must be a positive integer.")
    
    n = len(string_s)
    if length_l > n:
        return []

    substrings_list = []
    
    # Pre-compute start indices to avoid recalculating the window boundary repeatedly during loop logic,
    # though in Python slicing is highly optimized, this ensures clarity of O(N-L+1) iterations.
    for i in range(n - length_l + 1):
        substrings_list.append(string_s[i : i + length_l])

    return substrings_list

if __name__ == '__main__':
    # Hard-coded sample values as per requirements: no user input, args, or network access.
    SAMPLE_STRING = "abcdefghij"
    SUBSTRING_LENGTH = 3

    result_substrings = extract_substrings(SAMPLE_STRING, SUBSTRING_LENGTH)

    print(f"Input String (S): {SAMPLE_STRING}")
    print(f"Target Length (L): {SUBSTRING_LENGTH}")
    print("Extracted Substrings:")
    for sub in result_substrings:
        print(f"  '{sub}'")