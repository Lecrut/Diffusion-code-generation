import timeit

def extract_substrings_sliding_window(S: str, L: int) -> list[str]:
    """
    Extract all substrings of length L from string S using a sliding window technique.
    
    This function uses an optimized approach with O(n * l) complexity where n is the 
    length of the input string and l is the substring length (L). It avoids repeated 
    slicing operations by maintaining a fixed-length buffer or using Python's efficient 
    slice notation directly, which internally optimizes memory allocation.
    
    Parameters:
        S (str): The input string from which substrings are extracted.
        L (int): The desired length of each substring. Must be positive and <= len(S).
        
    Returns:
        list[str]: A list containing all contiguous substrings of length L found in S.
        
    Raises:
        ValueError: If L is not a valid integer or if it exceeds the string length.
        
    Time Complexity Analysis:
        - Generating each substring takes O(L) time due to character copying/slicing.
        - There are (n - L + 1) such substrings for an input of length n.
        - Total complexity is approximately O(n * l), which is optimal since every 
          output character must be processed at least once.
    """
    if not isinstance(L, int):
        raise TypeError("Length parameter 'L' must be an integer.")
    
    if L <= 0:
        raise ValueError("Length parameter 'L' must be a positive integer.")
        
    n = len(S)
    
    # If the window size is larger than or equal to the string length, 
    # return only one substring (or handle edge case explicitly).
    if L > n:
        return []
        
    result_list = []
    
    for i in range(n - L + 1):
        result_list.append(S[i : i+L])

    return result_list

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input.
    SAMPLE_INPUT_STRING = "abcdefghij"
    DESIRED_SUBSTRING_LENGTH = 3
    
    # Execute function call with hardcoded parameters.
    substrings = extract_substrings_sliding_window(SAMPLE_INPUT_STRING, DESIRED_SUBSTRING_LENGTH)
    
    print("Input String:", repr(SAMPLE_INPUT_STRING))
    print(f"Substring Length: {DESIRED_SUBSTRING_LENGTH}")
    print("Extracted Substrings:")
    for sub in substrings:
        print(repr(sub), end=" ")
        
    # Additional test case with duplicate characters to verify correctness.
    SAMPLE_TEST2 = "aabbaaabb"
    LATEST_L = 4
    
    result_test_2 = extract_substrings_sliding_window(SAMPLE_TEST2, LATEST_L)
    
    print("\nTest Case 2:")
    print("Input:", repr(SAMPLE_TEST2))
    print(f"Length: {LATEST_L}")
    print(substring_list := [sub for sub in result_test_2]) # Store as list comprehension logic check.