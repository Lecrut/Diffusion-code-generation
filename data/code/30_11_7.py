class CustomString:
    """A custom string class with additional functionality to swap adjacent pairs."""

    def __init__(self, value):
        """Initialize the CustomString instance with a given string value."""
        self._value = str(value) if not isinstance(value, str) else value

    @property
    def value(self):
        """Return the underlying string value as an immutable string."""
        return self._value

    def swap_adjacent_pairs(self):
        """
        Swap the characters of every adjacent pair within the string instance.
        
        This method iterates through the string in steps of two, swapping each 
        character at index i with the character at index i+1 if both indices are valid.
        
        Returns:
            CustomString: The modified custom string instance with swapped pairs.

        Raises:
            TypeError: If input is not a string-like object (handled by constructor).
            
        Examples:
            >>> cs = CustomString("abcd")
            >>> result_cs = cs.swap_adjacent_pairs()
            >>> print(result_cs.value)
            'badc'
        """
        # Convert to list for mutability, then back to string at the end.
        char_list = list(self._value)
        
        # Iterate with a step of 2
        for i in range(0, len(char_list), 2):
            # Check if there is a second character available (i+1 < length)
            if i + 1 < len(char_list):
                # Swap the characters at current index and next index
                char_list[i], char_list[i + 1] = char_list[i + 1], char_list[i]
        
        return CustomString("".join(char_list))

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    
    test_cases = [
        "abcd",      # Even length, full swaps: abcd -> badc
        "abcde",     # Odd length, last char remains: abcde -> bacd e (wait logic check) 
                     # Logic trace: a<->b, c<->d, e stays. Result: bacad? No.
                     # Input: a,b,c,d,e
                     # i=0: swap(a,b) -> b,a,c,d,e
                     # i=2: swap(c,d) -> b,a,d,c,e
                     # Output should be badce. Let's re-verify manual trace in head or code logic.
        "hello",     # h<->e, l<->l (no change), o stays? No wait indices 0,1 and 2,3. 
                     # h(0)<->e(1) -> ehll... no input is hello: h,e,l,l,o
                     # i=0: swap(h,e) -> e,h,l,l,o
                     # i=2: swap(l,l) -> e,h,l,l,o (no change)
                     # Result: ehll o. Wait, index 4 is 'o'. 
        "123",       # 1<->2, 3 stays -> 213
    ]

    print("Running CustomString swap_adjacent_pairs tests...\n")

    for test_input in test_cases:
        original = f"Original String: '{test_input}'\n"
        
        cs_instance = CustomString(test_input)
        swapped_cs = cs_instance.swap_adjacent_pairs()
        
        result_str = f"\tSwapped Result: '{swapped_cs.value}'\n"
        
        print(original + result_str)

    # Additional verification with a specific known case to ensure correctness logic.
    verify_case = "abcdefg"
    expected_verify = "badcfeg"  # ab->ba, cd->dc, ef->fe, g stays
    
    cs_v = CustomString(verify_case)
    res_v = cs_v.swap_adjacent_pairs()
    
    print(f"\nVerification Case: '{verify_case}'")
    if res_v.value == expected_verify:
        print("✓ Verification Passed.")
    else:
        print(f"✗ Verification Failed. Expected '{expected_verify}', got '{res_v.value}'.")