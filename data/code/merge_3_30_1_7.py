def swap_adjacent_pairs(s: str) -> str:
    """
    Returns a new string where every pair of adjacent characters has been swapped.
    
    Uses slicing to efficiently construct the result by taking even-indexed 
    and odd-indexed characters separately, then concatenating them in reverse order 
    relative to their original pairing (even chars from odds, odd chars from evens).
    
    Args:
        s (str): The input string.
        
    Returns:
        str: A new string with adjacent character pairs swapped.
    """
    if len(s) % 2 == 1:
        # If the length is odd, we swap all complete pairs and keep the last char as is.
        return s[:-1][::2] + s[-1:] + s[:len(s)-1][::-2]

    even_chars = s[0:len(s):2]
    odd_chars = s[1:len(s):2]
    
    # Swap pairs: take first half of evens with last half of odds, then second half...
    # Actually simpler logic for full swap: 
    # Pair (s[i], s[i+1]) becomes (s[i+1], s[i]).
    # We can achieve this by taking characters at odd positions and even positions.
    
    return ''.join(list(odd_chars) + list(even_chars))

if __name__ == '__main__':
    test_cases = [
        "abcdef",
        "ab",
        "",
        "a",
        "1234567890"
    ]

    for case in test_cases:
        result = swap_adjacent_pairs(case)
        print(f'Input: "{case}" -> Output: "{result}"')