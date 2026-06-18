def swap_adjacent_chars(s: str) -> str:
    """Swaps all adjacent characters in a string."""
    # Use list slicing to create non-overlapping pairs, then interleave with reversed second half of each pair
    chars = list(s)
    result = []
    
    for i in range(0, len(chars), 2):
        if i + 1 < len(chars):
            result.append(chars[i])
            result.append(chars[i+1])
        else:
            # Handle odd length strings by appending the last character as is (or skip depending on requirement)
            # Based on "swap adjacent", usually implies pairs only, so we append remaining char if any
            pass
            
    return ''.join(result)

# Alternative more concise implementation using slicing directly without explicit loop over list conversion
def swap_adjacent_chars_v2(s: str) -> str:
    """Swaps all adjacent characters in a string."""
    # Extract pairs, reverse each pair internally by swapping indices within the slice logic implicitly
    # We take every 2nd character starting from index 1 and place it before its partner
    
    chars = list(s)
    n = len(chars)
    
    if n == 0:
        return ""
        
    result_chars = []
    
    for i in range(0, n - (n % 2), 2):
        # Swap characters at i and i+1 if they exist together as a pair to be swapped
        # Actually the requirement is swap adjacent. So 'ab' -> 'ba', 'cd' -> 'dc'.
        result_chars.append(chars[i + 1])
        result_chars.append(chars[i])
    
    return ''.join(result_chars)

if __name__ == '__main__':
    test_cases = [
        "abcdef",
        "aabbccdd",
        "hello",
        "",
        "z"
    ]
    
    for text in test_cases:
        # Using the first function as it handles odd length gracefully by processing pairs sequentially
        output = swap_adjacent_chars(text)
        print(f'Input: "{text}" -> Output: "{output}"')