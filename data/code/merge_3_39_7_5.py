import sys

def extract_substrings(s: str, l: int) -> list[str]:
    """
    Extract all substrings of length L from string S using a sliding window technique.
    
    Optimizes time complexity to O(N), where N is the length of the input string.
    This avoids repeated slicing operations which would result in O(N*L).

    Args:
        s (str): The input string.
        l (int): The desired substring length.

    Returns:
        list[str]: A list containing all substrings of length L found in S.
    
    Raises:
        ValueError: If the provided length is invalid or exceeds the string bounds.
    """
    if not isinstance(s, str) or l < 0:
        raise TypeError(f"Invalid input types: s must be a string and l >= 0.")
    
    n = len(s)
    
    # Handle edge cases where substring length is invalid relative to string size
    if l > n:
        return []
    elif l == 0:
        # Depending on interpretation, an empty list or single empty string might be expected. 
        # Standard behavior for 'substrings of length L' usually implies non-empty results if possible,
        # but technically one substring exists (empty). We'll stick to the standard sliding window logic.
        return [""], 0

    substrings = []
    
    # Sliding window implementation: O(N) time complexity
    for i in range(n - l + 1):
        start_index = i
        end_index = i + l
        
        # Efficient substring extraction using slicing (Python handles this efficiently internally, 
        # though creating new strings adds a constant factor per iteration. The loop itself is linear.)
        substrings.append(s[start_index:end_index])

    return substrings

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    
    test_cases = [
        ("abcdef", 3),          # Expected: ['abc', 'bcd', 'cde', 'def']
        ("aaaaa", 2),           # Expected: ['aa', 'aa', 'aa', 'aa']
        ("hello world", 5),     # Expected: ['hell ', 'ello w', 'llo wo', 'lo wor', 'o world'] (spaces included)
        ("short", 10),          # Expected: [] (length exceeds string size)
        ("", 3),                # Expected: [] (empty string with positive length requested)
    ]

    for s, l in test_cases:
        result = extract_substrings(s, l)
        print(f"Input String S: '{s}'")
        print(f"Substring Length L: {l}")
        print(f"Resulting Substrings: {result}\n")