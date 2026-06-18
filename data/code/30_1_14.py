def swap_adjacent_pairs(s: str) -> str:
    """
    Returns a new string where every pair of adjacent characters has been swapped.
    
    Uses slicing to process pairs efficiently without modifying the original string in place.
    For even-length strings, it swaps all complete pairs (s[0], s[1]), (s[2], s[3]), etc.
    For odd-length strings, the last character remains unchanged as there is no pair for it.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with adjacent characters swapped in pairs.
    """
    # Create a list of lists where each inner list contains two consecutive characters or just one if odd length
    result = []
    
    for i in range(0, len(s), 2):
        pair = s[i:i+2]
        # Swap the elements within the pair (e.g., "ab" becomes "ba", "a" stays "a")
        swapped_pair = list(reversed(pair))
        result.append("".join(swapped_pair))
    
    return "".join(result)

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies
    
    samples = [
        "abcdef",      # Expected: "bacdef" -> wait, let's trace carefully. 
                      # Pairs: (a,b)->ba, (c,d)->dc, (e,f)->fe => Result: badcf e? No.
                      # Let's re-verify logic with simple example "abcd": 
                      # i=0: pair="ab" -> reversed=["b","a"] -> append "ba"
                      # i=2: pair="cd" -> reversed=["d","c"] -> append "dc"
                      # Result for "abcd" is "badc". Correct.
        "abc",         # Expected: "bac" (last char 'c' has no partner, stays as is? 
                      # My logic above handles odd length by taking s[i:i+2] which gives 1 or 2 chars.
                      # If i=0 ("ab") -> swap to "ba". Next i=2 ('c') -> pair="c" -> reversed=["c"] -> append "c". Result: "bac". Correct.)
        "",            # Empty string should return empty string
        "a",           # Single character, returns same character.
    ]

    for sample in samples:
        output = swap_adjacent_pairs(sample)
        print(f"Input: '{sample}' -> Output: '{output}'")