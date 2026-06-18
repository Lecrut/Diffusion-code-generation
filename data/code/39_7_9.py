"""
Module to extract all substrings of length L from a string S using 
a sliding window technique optimized for time complexity O(n).

The algorithm iterates through the string once, maintaining a fixed-size window
of characters and collecting each substring as it slides by one position.
This ensures linear time performance relative to the input string length.

Time Complexity: O(n), where n is the length of string S.
Space Complexity: O(k * m) for storing results, where k is the number of substrings 
                   (n - L + 1) and m is the average substring length (L).
"""

def extract_substrings(string_s: str, window_length_l: int):
    """
    Extracts all contiguous substrings of a specified length from an input string.

    Args:
        string_s (str): The source string to process.
        window_length_l (int): The desired length for each substring. Must be 
                               positive and not greater than the string length.

    Returns:
        list[str]: A list containing all substrings of the specified length.
                   If the input is empty or L > len(S), returns an empty list.

    Raises:
        ValueError: If window_length_l is less than 1 or exceeds the string's length,
                    ensuring robustness against invalid configurations.
    
    Example Usage (Internal):
        >>> extract_substrings("ABC", 2)
        ['AB', 'BC']
    """
    if len(string_s) == 0:
        return []

    # Input validation to ensure logic remains safe and predictable
    if window_length_l < 1 or window_length_l > len(string_s):
        raise ValueError(f"window_length must be >= 1 and <= length of string. "
                         f"Got L={window_length_l}, Length S={len(string_s)}")

    substrings = []
    
    # Sliding window logic: Iterate only up to n - l + 1 positions
    for i in range(len(string_s) - window_length_l + 1):
        substring = string_s[i : i + window_length_l]
        substrings.append(substring)

    return substrings

if __name__ == '__main__':
    # Hard-coded sample values as per requirements; no user input or file access.
    
    test_cases = [
        ("HelloWorld", 3),      # Expected: ['Hel', 'ell', 'llo', 'lor', 'ord']
        ("Python", 2),          # Expected: ['Py', 'yo', 'on', 'nt']
        ("AAAAA", 1),           # Expected: ['A', 'A', 'A', 'A', 'A']
        ("Short", 5)            # Edge case matching length exactly
    ]

    for string_s, l in test_cases:
        try:
            result = extract_substrings(string_s, l)
            print(f"Input String: '{string_s}', Length L={l}")
            print(f"Extracted Substrings ({len(result)} found):")
            for sub in result:
                print(sub)
            print("-" * 20)
        except ValueError as ve:
            print(f"Error processing input: {ve}")
    
    # Specific test case from docstring example
    specific_test = ("ABC", 2)
    res_specific = extract_substrings(*specific_test)
    assert 'AB' in res_specific and 'BC' in res_specific, "Specific assertion failed."