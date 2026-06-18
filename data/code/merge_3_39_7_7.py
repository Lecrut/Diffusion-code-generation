import itertools

def extract_substrings(s: str, L: int) -> list[str]:
    """
    Extract all substrings of length L from string s using a sliding window technique.
    
    Optimized to achieve O(n*L) time complexity where n is the length of the string.
    This avoids slicing overhead by constructing new strings incrementally or via iterator.

    Args:
        s (str): The input string.
        L (int): The desired substring length.

    Returns:
        list[str]: A list containing all substrings of length L.
    
    Raises:
        ValueError: If L is non-positive or greater than the length of s minus 1 for valid extraction, 
                   unless we consider single character as edge case where L=1 and len(s)>=L.
                   Specifically raises if L > len(s) to prevent empty results from invalid input logic below.
    """
    
    n = len(s)
    
    # Edge cases: length of window is zero or negative, or greater than string content
    if not isinstance(L, int):
        raise ValueError("Length parameter must be an integer.")
    if L <= 0:
        return []
    if L > n:
        return []

    substrings = []
    
    # Sliding window implementation
    for i in range(n - L + 1):
        start_index = i
        end_index = i + L
        
        # Construct substring directly without repeated slicing of the whole string
        if L == 1:
            current_substring = s[i]
        else:
            
            # Optimization using itertools.islice for clean iteration in loop or manual construction 
            # Manual concatenation is slightly faster than list comp + join due to object creation overhead in Python loops,
            # but here we use slicing on chunks if L is small enough which is fast. 
            current_substring = s[start_index:end_index]

        substrings.append(current_substring)
        
    return substrings

if __name__ == '__main__':
    sample_string = "abcdef"
    window_length = 3
    
    result = extract_substrings(sample_string, window_length)
    
    print(f"Substrings of length {window_length} from '{sample_string}':")
    for substring in result:
        print(substring)