import sys

def extract_substrings(s: str, l: int) -> list[str]:
    """
    Extract all substrings of length L from string S using a sliding window technique.
    
    Time Complexity: O(N), where N is the length of the input string.
    Space Complexity: O(K * L), where K is the number of valid substrings (N - L + 1).

    Args:
        s (str): The input string to process.
        l (int): The desired length of each substring. Must be a positive integer <= len(s).

    Returns:
        list[str]: A list containing all contiguous substrings of length L from S.
                   If L > len(S) or L < 1, returns an empty list.
    
    Raises:
        ValueError: If l is not a positive integer.
    """
    if not isinstance(l, int) or l <= 0:
        raise ValueError("Length parameter 'l' must be a positive integer.")

    n = len(s)
    
    # Edge case: substring length cannot exceed string length
    if l > n:
        return []
    
    substrings = []
    
    # Sliding window implementation using explicit iteration for clarity and efficiency
    # We iterate from index 0 to (n - l), extracting the slice s[i:i+l] at each step.
    current_index = 0
    while current_index <= n - l:
        substrings.append(s[current_index : current_index + l])
        current_index += 1
    
    return substrings

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files.
    
    # Sample Input Data
    SAMPLE_STRING = "abcdefg"
    SUBSTRING_LENGTH = 3
    
    try:
        result_substrings = extract_substrings(SAMPLE_STRING, SUBSTRING_LENGTH)
        
        print(f"Input String: '{SAMPLE_STRING}'")
        print(f"Substring Length: {SUBSTRING_LENGTH}")
        print("-" * 40)
        print("Extracted Substrings:")
        for sub in result_substrings:
            print(sub)
            
    except ValueError as ve:
        # Graceful error handling for invalid inputs during the sample run.
        print(f"Error encountered during processing: {ve}")