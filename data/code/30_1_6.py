def swap_adjacent_pairs(s: str) -> str:
    """
    Returns a new string where every pair of adjacent characters has been swapped.
    
    If there is an odd number of characters, the last one remains in place.
    Uses slicing for optimal performance.
    
    Args:
        s (str): The input string to process.
        
    Returns:
        str: A new string with every pair of adjacent characters swapped.
    """
    if len(s) == 0:
        return ""
    
    # Split the string into pairs and reverse each pair, then join them back together.
    # Using slicing to extract non-overlapping two-character chunks efficiently.
    result = []
    for i in range(0, len(s), 2):
        if i + 1 < len(s):
            result.append(f"{s[i+1]}{s[i]}")
        else:
            # Handle the case where there is an odd-length string left over.
            result.append(s[i])
    
    return "".join(result)

if __name__ == '__main__':
    test_cases = [
        "abcdef",       # Even length, full swaps -> "bacdef" (wait: b,a c,d e,f? No: a,b->ba; c,d->dc; e,f->fe. Input abcdef -> badc fe)
                       # Correction logic trace: 
                       # i=0: s[1]s[0] = 'b','a' -> "ba"
                       # i=2: s[3]s[2] = 'd','c' -> "dc"
                       # i=4: s[5]s[4] = 'f','e' -> "fe"
                       # Result: "badcf e"? No. 
                       # Input: a b c d e f
                       # Pair 1 (0,1): ba
                       # Pair 2 (2,3): dc
                       # Pair 3 (4,5): fe
                       # Output: badcfe? Wait. "ba" + "dc" + "fe" = "badcf e"? No. 
                       # Let's re-verify the expectation for input "abcdef".
                       # Indices: 0:a, 1:b -> swap to b,a.
                       # Indices: 2:c, 3:d -> swap to d,c.
                       # Indices: 4:e, 5:f -> swap to f,e.
                       # Result string: "badcfe". 
        "abc",          # Odd length -> bac + c = "bca" (a,b->ba; c stays)
        "",             # Empty string
        "x",            # Single character -> x
    ]

    for test_input in test_cases:
        print(f"Input: '{test_input}'")
        output = swap_adjacent_pairs(test_input)
        print(f"Output: '{output}'\n")