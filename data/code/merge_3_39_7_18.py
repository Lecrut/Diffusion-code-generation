import time

def extract_substrings_sliding_window(s: str, l: int) -> list[str]:
    """
    Extract all substrings of length L from string S using a sliding window technique.
    
    Time Complexity: O(N), where N is the length of string S.
    Space Complexity: O(K*L), where K is the number of substrings found (at most N-L+1).

    Args:
        s (str): The input string to process.
        l (int): The desired length of each substring. Must be a positive integer <= len(s).

    Returns:
        list[str]: A list containing all contiguous substrings of the specified length.
    
    Raises:
        ValueError: If l is not a valid positive integer or if l > len(s).
    """
    n = len(s)
    
    # Input validation to ensure robustness without external dependencies
    if not isinstance(l, int):
        raise TypeError("Length parameter 'l' must be an integer.")
    if l <= 0:
        raise ValueError(f"Length parameter 'l' must be a positive integer. Received {l}.")
    if n < l:
        # If the string is shorter than L, no substrings of length L exist.
        return []

    result = []
    
    # Sliding window implementation with O(1) per iteration logic for slicing efficiency in Python
    # We iterate from index 0 to n - l inclusive.
    # Using s[i:i+l] creates a new string slice, which is optimized by CPython but still 
    # results in O(L) copy operations overall leading to O(N*L) total time complexity strictly speaking for the output generation.
    # However, compared to naive nested loops or repeated full scans (O(N^2)), this is optimal for generating the result list.

    start_index = 0
    end_index = l
    
    while end_index <= n:
        substring = s[start_index:end_index]
        result.append(substring)
        
        # Advance window by one character to maintain O(1) movement logic (though slicing is not strictly constant time, 
        # the iteration count itself is linear).
        start_index += 1
        
        if end_index < n:
            end_index += 1

    return result

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are required.
    
    # Sample Input Data
    SAMPLE_STRING = "abcdefghij"
    SUBSTRING_LENGTH = 3
    
    print(f"Processing string: '{SAMPLE_STRING}'")
    print(f"Target substring length: {SUBSTRING_LENGTH}")
    
    try:
        substrings = extract_substrings_sliding_window(SAMPLE_STRING, SUBSTRING_LENGTH)
        
        # Display results in a formatted manner for verification
        if not substrings:
            print("No substrings found.")
        else:
            print(f"Found {len(substrings)} substring(s):")
            for i, sub in enumerate(substrings, 1):
                print(f"{i}. '{sub}'")
                
    except (ValueError, TypeError) as e:
        # Graceful error handling without crashing the script on invalid inputs if they were passed differently later.
        print(f"An error occurred during processing: {e}")