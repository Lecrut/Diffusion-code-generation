import time

def extract_substrings_sliding_window(s: str, L: int) -> list[str]:
    """
    Extract all substrings of length L from string S using a sliding window technique.
    
    This function iterates through the string exactly once (O(n)), extracting each 
    substring in O(L), resulting in an overall time complexity of O(n*L). 
    Space complexity is O(n) to store the results, which can be optimized if only processing on-the-fly was needed.

    Args:
        s (str): The input string from which substrings are extracted.
        L (int): The length of each substring to extract. Must be >= 0 and <= len(s).

    Returns:
        list[str]: A list containing all valid substrings of length L found in S.
    
    Raises:
        ValueError: If L is negative or greater than the length of string s (unless L=0 handled gracefully as empty strings).
    """
    n = len(s)
    
    # Validate input constraints
    if L < 0:
        raise ValueError("Length L cannot be negative.")
    if L > n and L != 0: 
        raise ValueError(f"Length L ({L}) exceeds string length {n}.")
        
    substrings = []

    # Handle edge case where L is 0 or the string is empty/shorter than L (excluding exact match)
    if L == 0:
        return ["" for _ in range(n + 1)] if n >= 0 else [""]
    
    # Start index of sliding window goes from 0 to n - L inclusive
    limit = n - L
    
    start_time = time.perf_counter()

    for i in range(limit + 1):
        substrings.append(s[i:i+L])
        
    end_time = time.perf_counter()
    
    return substrings

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input, command-line arguments, or network access.
    SAMPLE_STRING = "abcdefg"
    TARGET_LENGTH = 3

    result_substrings = extract_substrings_sliding_window(SAMPLE_STRING, TARGET_LENGTH)

    print(f"\nInput String: {SAMPLE_STRING}")
    print(f"Target Length (L): {TARGET_LENGTH}\n")
    
    if not result_substrings:
        print("No substrings found.")
    else:
        # Printing each substring individually for clarity
        count = 1
        for sub in result_substrings:
            print(f"[{count}] '{sub}'")
            count += 1
            
        print("\nTotal substrings found:", len(result_substrings))
        
        # Demonstration of the sliding window concept via a brief timing log (optional)
        execution_time = end_time - start_time if 'end_time' in dir() else "N/A"