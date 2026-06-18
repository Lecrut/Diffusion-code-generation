def swap_even_odd_indices(s: str) -> str:
    """
    Swaps characters at even indices with their neighbors (odd indices).
    Handles strings of any length, including odd lengths.
    
    Parameters:
        s (str): Input string
    
    Returns:
        str: String with characters swapped between even and odd indices
    """
    if not s or len(s) == 1:
        return s

    result_list = list(s)
    # Only need to iterate through the first half of even positions
    for i in range(0, len(result_list), 2):
        j = i + 1  # Corresponding odd index
        
        if i < len(result_list) and j < len(result_list):
            result_list[i], result_list[j] = result_list[j], result_list[i]

    return ''.join(result_list)

if __name__ == '__main__':
    # Sample test cases without user input
    sample_strings = [
        "abcdef",          # Even length: a-f -> b-a, c-d, e-f becomes b,a,c,d,e,f? No wait.
                          # Original indices: 0:a,1:b,2:c,3:d,4:e,5:f
                          # Swap (even with next odd): 
                          # index 0(a) <-> 1(b), index 2(c)<->3(d), index 4(e)<->5(f)
                          # Result should be: b a d c f e
    
        "abc",             # Odd length: last char stays alone if no pair exists? 
                          # Wait, task says "swap characters at even indices with the characters at odd indices"
                          # Usually implies swapping i and i+1. If i is max index (odd), can't swap out to next.
                          # Let's assume we only swap valid pairs (i.e., both exist) or handle boundary carefully.
                          # Standard interpretation: iterate even i, if i+1 exists, swap(i, i+1).
    
        "x",               # Single character -> returns itself
    
        "aabbcc"           # 0<->1(a,b), 2<->3(b,a), 4<->5(c,c) -> baab c c -> b a a b c c? 
                          # Let's trace:
                          # i=0('a'), j=1('b') -> swap -> 'ba'...
                          # i=2('c'), j=3('d'? no, input is "aabbcc")
                          # 0:a, 1:a, 2:b, 3:b, 4:c, 5:c
                          # Swap: (0,a)<->(1,a) -> aa. (2,b)<->(3,b) -> bb. (4,c)<->(5,c)->cc. 
                          # Result: aabb cc? Actually since chars are same it looks same but indices moved.
    ]

    print("Input | Output")
    for test_str in sample_strings:
        output = swap_even_odd_indices(test_str)
        print(f"{test_str!r} : {output!r}")