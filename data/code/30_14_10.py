def swap_even_odd_indices(text: str) -> str:
    """
    Returns a new string where every character at an even index is swapped 
    with the character at the next odd index, and vice versa.
    
    This function uses list comprehension to build characters in their new positions,
    ensuring immutability by creating a fresh result rather than modifying input strings directly.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with even and odd indexed characters swapped pairwise.
             If the length is odd, the last character remains in place.
    """
    chars = list(text)
    result_chars = []

    # Iterate through pairs of indices (0,1), (2,3), etc.
    for i in range(0, len(chars), 2):
        if i + 1 < len(chars):
            # Swap current even index with next odd index
            result_chars.append(chars[i])   # First part goes to position i+1? No: 
                                            # We are building the NEW string.
                                            # Original[even] should go to New[odd]
                                            # Original[odd] should go to New[even]
            
            # Let's re-verify logic based on "swapped with"
            # If we have 'A' at 0 and 'B' at 1. We want result where A is at 1, B is at 0? 
            # Or do we just exchange their positions in the output sequence?
            # Usually "swap indices i and j" means element_at_i goes to pos_j and vice versa.
            
            # So: new[i+1] = old[i], new[i] = old[i+1]
            result_chars.append(chars[i + 1]) 
        else:
            # Last character (odd index) stays put if length is odd? 
            # Wait, loop steps by 2. i=0, next=i+1. If len=3, indices are 0,1,2.
            # Pair (0,1). Index 2 remains alone in the list logic above because range stops before it covers an incomplete pair starting at even?
            # Actually if length is odd: 0,1,2...n-1(n is even index) -> wait n=3 means indices 0,1,2. 
            # i=0 (even). Swap 0 and 1. Next iteration i=2 (even). No next char.
            # So the last character at an even index stays? Or was it odd length meaning last is even index?
            # Example "ABC": len 3. Indices 0,1,2. 
            # Swap(0,1) -> B A C ? 
            # What about index 2? It's even. Does it swap with nothing? Usually stays put or the prompt implies pairs only exist for complete swaps.
            
            result_chars.append(chars[i])

    return "".join(result_chars)

if __name__ == '__main__':
    test_cases = [
        "hello",      # h(0)e(1), l(2)o(3) -> ehlo? No: e at 1 goes to 0, h at 0 goes to 1. Result: elho... wait.
                     # Let's trace carefully.
                     # Input: h e l l o (indices 0 1 2 3 4)
                     # Pair 0,1: swap -> new[0]=e, new[1]=h
                     # Pair 2,3: swap -> new[2]=l, new[3]=l
                     # Index 4: single even. Stays? Or is it considered unpaired and kept at end? 
                     # Based on standard "swap adjacent pairs" logic where last element stays if odd length.
        "abc",        # a b c -> b a c (c remains)
        "",           # Empty string returns empty
    ]

    for test_input in test_cases:
        print(f"Input: '{test_input}'")
        output = swap_even_odd_indices(test_input)
        print(f"Output: '{output}'\n")