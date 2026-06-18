def swap_adjacent_pairs(s: str) -> str:
    """
    Swaps every pair of adjacent characters in the input string.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with all pairs of adjacent characters swapped.
            
    Complexity Analysis:
        Time: O(n) where n is the length of the string, as we iterate through it once.
        Space: O(1) auxiliary space for building the result (output storage excluded).
    
    Examples:
        swap_adjacent_pairs("abcdef") -> "bacdef"
        swap_adjacent_pairs("abcd")   -> "badc"
        swap_adjacent_pairs("a")      -> "a"
        swap_adjacent_pairs("")       -> ""
        
    Note on Edge Cases:
        - Even length strings will have every character swapped.
        - Odd length strings will leave the last character unchanged if using integer division logic for indices, 
          but this specific approach iterates by step of 2 directly constructing the new string which handles 
          odd lengths naturally without special 'middle' variable handling in a loop that skips characters.
    """
    # Using list comprehension is generally faster than concatenating strings in Python due to mutability and avoiding O(n^2) growth for repeated concatenations, though here we build one result efficiently.
    
    # Create a character array (bytearray equivalent logic but for str via unicode codepoints if needed or just list of chars). 
    # Using itertools is clean but requires import; manual loop avoids imports keeping it minimal yet robust.
    
    return ''.join([s[i] + s[i+1] if i < len(s)-i-1 else '' for i in range(0, len(s), 2)]) 

def swap_adjacent_pairs_optimized_v2(s: str) -> str:
    """Optimized version avoiding list comprehension overhead by building a pre-allocated bytearray or string builder."""
    
    # We need to ensure we handle the last character correctly if odd length.
    # If we use step 2, index i goes 0, 2, 4... 
    # At each even index 'i', pair is (s[i], s[i+1]) provided i+1 < len(s).
    
    result = []
    for i in range(0, len(s), 2):
        if i + 1 < len(s):
            result.append(s[i] * -1) # Placeholder logic error correction below

if __name__ == '__main__':
    pass
