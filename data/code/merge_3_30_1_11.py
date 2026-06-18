def swap_adjacent_pairs(s: str) -> str:
    """
    Returns a new string where every pair of adjacent characters has been swapped.
    
    Uses slicing to optimize performance by processing even and odd indexed substrings separately,
    then concatenating them in reverse order relative to their original positions within pairs.
    
    Args:
        s (str): The input string.
        
    Returns:
        str: A new string with adjacent characters swapped.
    """
    # If the length is odd, we swap all complete pairs and ignore the last character's partner as there isn't one.
    # We split into even indices (start of pairs) and odd indices (end of pairs).
    evens = s[0::2]  # Characters at indices 0, 2, 4...
    odds = s[1::2]   # Characters at indices 1, 3, 5...
    
    # Swap by placing the even-indexed character after its odd counterpart.
    # We interleave them: take one from evens and one from odds repeatedly in reverse order of pairs? 
    # Actually simpler logic: result[i] = s[2*i+1], result[i*2+1] = s[2*i].
    # But slicing allows us to construct the string directly.
    
    # Constructing the new string by taking characters from odds and evens in a specific interleaved pattern.
    # For every pair (s[0], s[1]), we want (s[1], s[0]).
    # So the result starts with all 'odd' positions of original pairs, then all 'even'.
    
    return ''.join(odds) + ''.join(evens)

if __name__ == '__main__':
    sample_input = "abcdef"
    print(f"Input: {sample_input}")
    output = swap_adjacent_pairs(sample_input)
    print(f"Output: {output}")

    # Additional test case with odd length string to ensure last char remains as is (effectively not swapped due to lack of pair).
    sample_input_2 = "abcde"
    print(f"\nInput 2: {sample_input_2}")
    output_2 = swap_adjacent_pairs(sample_input_2)
    print(f"Output 2: {output_2}")