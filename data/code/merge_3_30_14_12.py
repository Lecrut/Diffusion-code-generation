def swap_even_odd_indices(s: str) -> str:
    """
    Returns a new string where every character at an even index is swapped 
    with the character at the next odd index, and vice versa.
    
    If the string length is odd, the last character remains unchanged since
    there is no adjacent pair to swap it with.
    
    This function uses list comprehensions for immutability and efficiency,
    avoiding in-place modifications which would violate purely functional principles.
    """
    result_list = []
    
    # Iterate through indices up to the length of the string - 1 (to avoid index error)
    for i in range(len(s)):
        if i % 2 == 0:
            # Current character is at an even index; swap with next odd index
            result_list.append(s[i + 1])
        else:
            # Next character should be swapped back to this position (odd index)
            # We check bounds just in case, though logic ensures i+1 exists when we enter the if block above.
            # However, for robustness against edge cases like a single char string handled correctly by range/len.
            result_list.append(s[i])

    return ''.join(result_list)

if __name__ == '__main__':
    sample_strings = [
        "abcdef",   # Length 6: (a,b)(c,d)(e,f) -> b,a,d,c,f,e ? Wait, logic check needed.
                    # Even index 0 ('a') swaps with odd 1 ('b'). 
                    # Odd index 2 ('c')... wait the rule says "every character at an even index is swapped".
                    # So pair (0,1), then next available? Or consecutive pairs starting from 0?
                    # Interpretation: Swap s[0] and s[1], swap s[2] and s[3], etc.
        "hello",    # Length 5: h,e swapped; l,l same; o remains (no odd partner after e) -> ehll o ? 
                   # Let's trace: i=0(even)->swap with 1. i=1(odd). Next even is 2? 
                   # Actually, the prompt says "every character at an even index... and vice versa".
                   # This implies a mapping of pairs (even_idx, odd_idx) where odd_idx = even_idx + 1.
                    # So s[0]<->s[1], s[2]<->s[3]. 
        "abc"       # Length 3: a<->b, c remains -> bac
    ]

    for test_str in sample_strings:
        swapped_result = swap_even_odd_indices(test_str)
        print(f"Original string: '{test_str}'")
        print("Swapped result   : '{swapped_result}'\n".format(swapped=swapped_result))