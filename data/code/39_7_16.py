import time

def extract_substrings(string_s: str, length_l: int) -> list[str]:
    """
    Extract all substrings of a given length L from string S using 
    an optimized sliding window technique with O(N) time complexity.

    Args:
        string_s (str): The input string to process.
        length_l (int): Desired substring length. Must be positive and <= len(S).

    Returns:
        list[str]: A list of substrings of the specified length in order of appearance.

    Raises:
        ValueError: If length is invalid (<= 0 or greater than string length).
    """
    if not isinstance(string_s, str) or not isinstance(length_l, int):
        raise TypeError("Invalid input types")
    
    n = len(string_s)
    
    # Validate length parameter based on problem constraints from prompt examples and logic
    if length_l <= 0:
        return []
    elif length_l > n:
        return []

    result_substrings_list = []

    # Initialize the window to contain the first L characters.

if __name__ == '__main__':
    pass
