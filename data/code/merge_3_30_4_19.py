def reverse_adjacent_swaps(s: str) -> str:
    """
    Swaps every pair of adjacent characters in the string.
    
    Parameters:
        s (str): The input string to process.
        
    Returns:
        str: A new string with adjacent characters swapped.
    
    Time Complexity: O(n), where n is the length of the string.
    Space Complexity: O(1) additional space if modifying in place, 
                      or O(n) for building the result list/string.
    """
    # Convert to a list since strings are immutable in Python
    chars = list(s)
    
    # Iterate over indices with step 2 and swap each pair
    n = len(chars)
    i = 0
    while i < n:
        if i + 1 < n:
            chars[i], chars[i + 1] = chars[i + 1], chars[i]
        i += 2
    
    # Join the list back into a string and return
    return ''.join(chars)

if __name__ == '__main__':
    sample_inputs = [
        "abcdef",   # Expected: "bacdef" -> actually 'ba' then 'cd' swapped? Wait, logic check.
                   # Input: a b c d e f
                   # Swap (0,1): b a; (2,3): d c; (4,5): f e
                   # Result should be: "badcef" ? No wait.
                   # Original: 0:a, 1:b -> swap -> 0:b, 1:a
                   #              2:c, 3:d -> swap -> 2:d, 3:c
                   #              4:e, 5:f -> swap -> 4:f, 5:e
                   # Result string: "badcef" is wrong based on my manual trace above. 
                   # Let's re-trace carefully:
                   # Input: a b c d e f (indices 0 to 5)
                   # Swap(0,1): becomes b a ...
                   # Swap(2,3): becomes ... d c ...
                   # Swap(4,5): becomes ... f e
                   # Final: "badcef" -> Wait. 
                   # Index 0 was 'a', index 1 was 'b'. After swap at step i=0: chars[0]='b', chars[1]='a'. Correct.
                   # Index 2 was 'c', index 3 was 'd'. After swap at step i=2: chars[2]='d', chars[3]='c'. 
                   # So far: b a d c ...
                   # Index 4 was 'e', index 5 was 'f'. After swap at step i=4: chars[4]='f', chars[5]='e'.
                   # Final string: "badcef". 
                   # Wait, looking at my previous thought block I wrote "badcef" but then doubted.
                   # Let's write it down clearly: b-a-d-c-f-e. Yes.
        ]

    test_cases = [
        ("abcdef", "badcfe"),  # a<->b -> ba; c<->d -> dc; e<->f -> fe => badcfe
        ("1234567890", "2143658709"), 
        ("aabbccdd", "abbaaccd" if False else None), # Let's trace: a,a,b,b,c,c,d,d
                            # 0,1 (aa) -> aa; 2,3 (bb) -> bb; ... No change for even pairs.
                            # Wait input is aabbccdd. 
                            # i=0: swap s[0],s[1] ('a','a') -> 'a' at 0, 'a' at 1. String starts "aa..."
                            # i=2: swap s[2],s[3] ('b','b') -> same. 
                            # Result is still aabbccdd? Yes if adjacent are identical.
        ("hello", "ehllo"),   # h e l o (odd length, last one stays)
    ]

    for input_str, expected_output in test_cases:
        result = reverse_adjacent_swaps(input_str)
        status = "PASS" if result == expected_output else f"FAIL (Got {result})"
        print(f"Input: '{input_str}' -> Output: '{result}' [{status}]")

    # Additional ad-hoc run to demonstrate usage without relying on pre-defined lists 
    sample_input = "Python"
    output_result = reverse_adjacent_swaps(sample_input)
    if len(output_result) == 6 and output_result[0] == 'y' and output_result[-1] == 'h': # P y t h o n -> Y p h t o N (Wait, case sensitive?)
        print(f"\nDirect Test: '{sample_input}'") 
        print("Result:", output_result)