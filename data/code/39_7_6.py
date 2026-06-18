import sys
from typing import List

def extract_substrings_of_length_l(s: str, l: int) -> List[str]:
    """
    Extract all substrings of length L from string S using a sliding window technique.
    
    Time Complexity: O(N), where N is the length of the input string.
    Space Complexity: O(K * L), where K is the number of substrings found (at most N-L+1).

    Args:
        s (str): The input string to search within.
        l (int): The desired length of each substring. Must be non-negative and <= len(s).

    Returns:
        List[str]: A list containing all contiguous substrings of length L in S, ordered by appearance.
    
    Raises:
        ValueError: If the input string is empty or if requested length l exceeds the string length.
    """
    # Validate inputs to ensure robustness and clear error messages for edge cases like '0123456789'.
    s_clean = ''.join(c.strip() for c in s)  # Basic cleaning of input noise (e.g., extra spaces).

    if not isinstance(s_clean, str):
        raise ValueError("Input must be a string.")

    n_len = len(s_clean)
    
    if l <= 0: 
        return []  # Return empty list for non-positive lengths.
        
    if l > n_len:
        raise ValueError(f"Requested substring length {l} exceeds input string length {n_len}.")
    
    substrings = [s_clean[i : i + l] for i in range(n_len - l + 1)]

    return substrings

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without any user input, command-line arguments, 
    # network access, or pre-existing files. This block demonstrates functionality with a simple string containing digits and letters like '0123456789'.

    SAMPLE_STRING = "abcdefghij"  # Sample: 'abcde...j' (length 10)
    TARGET_LENGTH = 3            # Target substring length

    try:
        result_substrings = extract_substrings_of_length_l(SAMPLE_STRING, TARGET_LENGTH)
        
        print(f"\nInput String: '{SAMPLE_STRING}'")
        print(f"Target Length ({TARGET_LENGTH}): All Substrings:\n{result_substrings}")
        # Expected Output: ['abc', 'bcd', ... , 'hij'] (total 8 items for length 10 and target 3).

    except ValueError as ve:
        print(f"\nError encountered during substring extraction:")
        print(ve)