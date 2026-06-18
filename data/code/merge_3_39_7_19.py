import timeit

def extract_substrings_sliding_window(s: str, l: int) -> list[str]:
    """
    Extract all substrings of length L from string S using a sliding window technique.
    
    Time Complexity: O(N), where N is the length of string S.
    Space Complexity: O(K * L), where K is the number of substrings found (N - L + 1).

    Args:
        s (str): The input string to process.
        l (int): The desired length of each substring. Must be a positive integer <= len(s).

    Returns:
        list[str]: A list containing all valid substrings of the specified length.
    
    Raises:
        ValueError: If L is not a positive integer or if L > len(S).
    """
    n = len(s)
    
    # Validate input parameters to ensure correctness and prevent runtime errors later
    if l <= 0 or l > n:
        raise ValueError(f"Length {l} must be a positive integer less than or equal to the string length ({n}).")

    substrings = []
    
    # Iterate through the string with a sliding window of size L.
    # We start from index 0 up to (inclusive) n - l, ensuring that each substring 
    # has exactly 'l' characters remaining in the original string after it starts.
    for i in range(n - l + 1):
        substrings.append(s[i : i + l])

    return substrings

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, command-line arguments, or network access is required.
    
    # Sample Input String and Substring Length
    SAMPLE_STRING = "abcdefghij"  # A string of length 10 for demonstration purposes.
    SUBSTRING_LENGTH = 3          # We want substrings of length 3.

    print(f"Processing input: '{SAMPLE_STRING}' with substring length {SUBSTRING_LENGTH}")
    
    try:
        result_substrings = extract_substrings_sliding_window(SAMPLE_STRING, SUBSTRING_LENGTH)
        
        print("Extracted Substrings:")
        for idx, sub in enumerate(result_substrings):
            print(f"  [{idx + 1}]: '{sub}'")
            
        # Demonstrate performance optimization by timing the operation on a larger dataset.
        LARGE_STRING = "x" * 50000  # A string of 50,000 characters to test efficiency.
        
        print("\nPerformance Test (Large Dataset):")
        start_time = timeit.default_timer()
        large_result = extract_substrings_sliding_window(LARGE_STRING, SUBSTRING_LENGTH)
        end_time = timeit.default_timer()
        
        execution_time_ms = (end_time - start_time) * 1000
        
        print(f"Processed {len(large_result)} substrings in {execution_time_ms:.2f} milliseconds.")
        # Verify correctness on the large dataset by checking a known substring.
        expected_first_substring = "xxxxx"[:SUBSTRING_LENGTH] if SUBSTRING_LENGTH <= 5 else LARGE_STRING[0:SUBSTRING_LENGTH]
        print(f"First extracted substring matches expectation? {large_result[0] == expected_first_substring}")

    except ValueError as ve:
        print(f"Error during processing: {ve}")