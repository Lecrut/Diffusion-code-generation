import sys

def extract_substrings(s: str, l: int) -> list[str]:
    """
    Extract all substrings of length L from string S using a sliding window technique.
    
    Time Complexity: O(N), where N is the length of the input string.
    Space Complexity: O(K * L), where K is the number of substrings found (N - L + 1).

    Args:
        s (str): The input string to process.
        l (int): The desired length of each substring.

    Returns:
        list[str]: A list containing all valid substrings of length L.
    
    Raises:
        ValueError: If the requested length is invalid or exceeds the string length.
    """
    if not isinstance(s, str) or not isinstance(l, int):
        raise TypeError("Input 's' must be a string and 'l' must be an integer.")
    
    n = len(s)
    
    # Validate constraints for substring extraction
    if l <= 0:
        raise ValueError(f"Length L ({l}) must be positive. Got non-positive value.")
    if l > n:
        raise ValueError(f"Requested length L ({L}) exceeds string length N ({n}).")

    result = []
    
    # Sliding window iteration from index 0 to (N - L) inclusive
    for i in range(n - l + 1):
        substring = s[i : i+l]
        result.append(substring)
        
    return result

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. No user input, CLI args, or network access used.
    
    # Sample Input Data
    SAMPLE_STRING = "abcdef"
    TARGET_LENGTH = 3
    
    try:
        substrings = extract_substrings(SAMPLE_STRING, TARGET_LENGTH)
        
        print(f"Input String '{SAMPLE_STRING}' with length {TARGET_LENGTH}:")
        for idx, sub in enumerate(substrings):
            print(f"[{idx}] -> '{sub}'")
            
    except ValueError as ve:
        # Handle validation errors gracefully during execution
        print(f"Error encountered: {ve}", file=sys.stderr)
        
    except Exception as e:
        # Catch any unexpected runtime exceptions to ensure clean exit
        print(f"Unexpected error occurred: {e}", file=sys.stderr)