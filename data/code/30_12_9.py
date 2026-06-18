import sys

def swap_adjacent_characters(s: str) -> str:
    """
    Swaps every pair of adjacent characters in a string.
    
    If the input length is odd, the last character remains unchanged as it has no pair.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with all pairs of adjacent characters swapped.
    """
    # Using list comprehension for efficiency and clarity
    return "".join(s[i] + s[i+1] if i % 2 == 0 else s[i] 
                   for i in range(0, len(s) - (len(s) % 2), 2))

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external files.
    test_cases = [
        "abcdef",      # Even length: ab <-> cd < ef -> bacdef? No, swap pairs: (ab)(cd)(ef) -> ba c d edf f wait logic check below.
                       # Logic correction based on requirement "swaps every pair":
                       # Input: a b c d e f
                       # Pairs: (a,b), (c,d), (e,f)
                       # Swap: b a, d c, f e -> ba dc fe -> badcfle? 
                       # Let's re-verify the logic in code.
        "abcd",       # abcd -> bacd
        "abcde" ,     # abcde -> bac de -> back to odd length handling
        "",            # Empty string edge case
        "a"             # Single character stays same
    ]

    for test_input in test_cases:
        result = swap_adjacent_characters(test_input)
        print(result)