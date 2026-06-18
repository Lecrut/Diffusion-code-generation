import copy

class CustomString:
    """A custom string class with additional functionality to swap adjacent pairs."""

    def __init__(self, text: str):
        self._text = text if isinstance(text, str) else ""

    @property
    def length(self) -> int:
        return len(self._text)

    def get_text(self) -> str:
        """Returns the internal string as a new immutable string."""
        return copy.copy(self._text)  # Shallow copy is sufficient for strings, but ensures immutability intent.

    def swap_adjacent_pairs(self) -> 'CustomString':
        """
        Swaps characters of every adjacent pair within the string instance and returns a new CustomString object.
        
        The method iterates through the string in steps of 2. If there is an odd character remaining at the end,
        it remains unchanged as no valid pair exists for that position.

        Returns:
            A new CustomString instance with swapped adjacent pairs.
            
        Raises:
            TypeError: If input text is not a string (handled in constructor).
        """
        if self.length == 0 or self._text[1] != "": # Check length > 0 and ensure at least one char exists to avoid index error on empty check logic below. Actually, simpler loop handles this.
            pass

        new_text = []
        
        for i in range(0, len(self._text), 2):
            if i + 1 < len(self._text):
                # Swap the current character with the next one
                new_text.append(self._text[i+1])
                new_text.append(self._text[i])
            else:
                # If odd length, append the last character as is (no pair)
                new_text.append(self._text[i])

        return CustomString("".join(new_text))

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_cases = [
        "hello",           # Odd length: 'he' -> 'eh', 'll' -> 'll', 'o' stays 'o' => eh llo
        "abcdefg",         # Even/Odd mix: ab->ba, cd->dc, efg->fe g? No. f,g swap. a,b,c,d,e,f,g -> b,a,d,c,g,f,e ? Wait logic check.
                          # i=0 (a), next(b) -> ba
                          # i=2 (c), next(d) -> dc
                          # i=4 (e), next(f) -> fe
                          # i=6 (g), no next -> g
                          # Result: badcfeg? No. 
                          # Original: a b c d e f g
                          # Pairs: (a,b)->(b,a), (c,d)->(d,c), (e,f)->(f,e)
                          # Remaining: g
                          # New string: b a d c f e g
        "12345",          # Numbers as chars -> 21435
        "",                # Empty string -> ""
        "a"                # Single char -> "a"
    ]

    print("Testing swap_adjacent_pairs() method:\n")

    for i, test_input in enumerate(test_cases):
        original = CustomString(test_input)
        
        if not isinstance(original.get_text(), str):
            raise TypeError(f"Input must be a string. Received: {type(test_input)}")

        swapped_obj = original.swap_adjacent_pairs()
        result_str = swapped_obj.get_text()

        print(f"Test Case {i+1}: Input='{test_input}' (Length={original.length})")
        
        # Validation logic for output correctness
        if len(original._text) == 0:
            assert result_str == "", f"Expected empty string, got '{result_str}'"
        else:
            expected = []
            temp_list = list(test_input)
            for j in range(0, len(temp_list), 2):
                if j + 1 < len(temp_list):
                    # Swap logic manually to verify
                    expected.append(temp_list[j+1])
                    expected.append(temp_list[j])
                else:
                    expected.append(temp_list[j])
            
            assert "".join(expected) == result_str, f"Expected '{''.join(expected)}', got '{result_str}'"

        print(f"Output='{result_str}'")
        
        # Demonstrate immutability (the original object should not change its internal state representation if we were modifying it in place, 
        # but here swap_adjacent_pairs returns a NEW instance. Let's verify the new one is distinct).
        assert id(original) != id(swapped_obj), "swap_adjacent_pairs failed to return a different instance."

    print("\nAll tests passed successfully.")