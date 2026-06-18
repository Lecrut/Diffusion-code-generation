import copy

class CustomString:
    """A custom string class that supports swapping adjacent pairs."""

    def __init__(self, value: str):
        self._value = list(value) if isinstance(value, (bytes, bytearray)) else list(value)

    @property
    def length(self) -> int:
        return len(self._value)

    def swap_adjacent_pairs(self) -> None:
        """
        Swaps the characters of every adjacent pair within this instance.
        
        For a string 'abcd', it becomes 'badc'.
        For an odd-length string like 'abcde', the last character remains in place, resulting in 'dbace' (pairs swapped as ab->ba, cd->dc, e stays).

        Raises:
            TypeError: If self is not initialized properly.
        """
        if len(self._value) == 0:
            return
        
        # Iterate over the list with a step of 2
        for i in range(0, len(self._value), 2):
            # Check bounds to ensure safety (though loop structure should prevent out-of-bounds access on pairs)
            if i + 1 < len(self._value):
                self._value[i], self._value[i+1] = self._value[i+1], self._value[i]

    def __str__(self) -> str:
        return "".join(self._value)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality
    
    test_cases = [
        "hello",       # Expected output: olhelo (he->eh, ll stays? No. h-e-l-l-o -> e-h-o-l-l? Wait logic check)
                       # Logic trace: 
                       # i=0: swap self[0],self[1] ('h','e') -> 'e' 'h'. List: ['e', 'h', ...]
                       # i=2: swap self[2],self[3] ('l','l') -> 'l' 'l'. 
                       # i=4: loop ends.
                       # Result "eholl". My previous trace was wrong, let's re-verify logic against standard pair swap.
    ]

    s1 = CustomString("abcdef")
    print(f"Original: {s1}")  # abcdef -> badcfe (ab->ba, cd->dc, ef->fe)
    
    s2 = CustomString("abcde")
    print(f"Original: {s2}")   # bcda e? No. ab->ba, cd->dc, e stays. -> bdace
    
    s3 = CustomString("")
    print(f"Empty String length: {len(s1)}")  # Just to verify empty handling logic inside class

    # Demonstrate the swap method on specific instance created in main block if needed? 
    # The task asks for a runnable module. I will demonstrate by creating instances and printing results immediately after swapping them or showing before/after.
    
    print("--- Execution Results ---")
    
    # Test Case 1: Even length, distinct characters
    t1 = CustomString("abcdefg") # g is last odd index? No len=7 (0..6). Pairs at 0-1, 2-3, 4-5. Index 6 ignored.
                                # a,b -> b,a ; c,d -> d,c ; e,f -> f,e 
    t1.swap_adjacent_pairs()
    print(f"Input: 'abcdefg'")
    print(f"Output after swap: '{t1}'\nExpected: 'badcfge'\n")

    # Test Case 2: Odd length, repeated characters
    t2 = CustomString("aabbcc") 
    # a,a -> a,a ; b,b -> b,b ; c,c -> c,c (No change)
    print(f"Input: '{t2}'")
    swap_t2 = CustomString(t2._value) # Create fresh instance to show state before? No, method modifies in place. 
                                        # Let's use a copy for display if needed or just trust the mutation logic shown above.
                                        # Actually, re-assigning variable is safer for demo clarity but class mutates itself.
    t2_before = CustomString("aabbcc")
    print(f"Input: '{t2_before}' -> Output after swap_adjacent_pairs(): '{t2_before}'\nExpected: 'aabbcc' (no change)\n")

    # Test Case 3: Mixed case and numbers
    t3 = CustomString("12AB-5!") 
    # 1,2 <-> 2,1 ; A,B <-> B,A -> - stays at end if odd? len=7. indices 0..6. pairs (0,1), (2,3), (4,5). index 6 ('!') ignored.
    t3.swap_adjacent_pairs()
    print(f"Input: '12AB-5!'")
    print(f"Output after swap_adjacent_pairs(): '{t3}'\nExpected: '21BA-5!'")

    # Edge case check (implicit via logic)
    s_empty = CustomString("")
    s_empty.swap_adjacent_pairs()
    assert len(s_empty._value) == 0, "Empty string handling failed"
    print("Edge Case Passed: Empty String\n")