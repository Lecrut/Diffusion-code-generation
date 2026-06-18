class CustomString:
    def __init__(self, value):
        """Initialize the custom string with a base value."""
        self.value = str(value) if not isinstance(value, str) else value

    def swap_adjacent_pairs(self):
        """
        Swaps the characters of every adjacent pair within the string instance.
        
        Logic: Iterates through the string in steps of two (0, 2, ...).
              If at least one character exists in a position {i, i+1}, it swaps them.
              
        Returns: A new CustomString with modified content; does not mutate original.
        """
        characters = list(self.value)
        
        # Iterate over the string in steps of 2 starting from index 0
        for i in range(0, len(characters), 2):
            if i + 1 < len(characters):
                # Swap adjacent pair (i and i+1)
                characters[i], characters[i + 1] = characters[i + 1], characters[i]
        
        return CustomString("".join(characters))

if __name__ == '__main__':
    test_cases = [
        "abcdefgh",      # Standard case: (ab, cd, ef, gh) -> (ba, dc, fe, hg)
        "abcde"          # Odd length ending with single char 'e' left unchanged relative to itself but not swapped since no pair
                        # Pairs are ab->ba, c->d swap? No. a<->b, c<->d leaves e alone if odd index without partner logic applied correctly per instructions "adjacent pair". 
                        # Strict interpretation: pairs only exist at (0,1), (2,3)... so 'e' is ignored in pairing process.
        "",              # Edge case empty string
        "xy",            # Minimum valid pair swap -> yx
        "xyzwuvwv"       # Even length test with repeating chars
    ]

    for original_value in test_cases:
        obj = CustomString(original_value)
        result_obj = obj.swap_adjacent_pairs()
        
        print(f"Original: '{original_value}'")
        print(f"Result   : '{result_obj.value}'\n")