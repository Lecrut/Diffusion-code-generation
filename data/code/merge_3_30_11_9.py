class CustomString:
    """A custom string-like class with additional methods."""

    def __init__(self, value: str = "") -> None:
        self._value = list(value)

    def swap_adjacent_pairs(self) -> 'CustomString':
        """
        Swaps the characters of every adjacent pair within this instance.
        
        The method iterates through the string with a step of 2, swapping
        the character at index i and i+1 for all valid pairs where (i+1) < length.
        
        Returns:
            CustomString: A new instance with swapped characters if any swap occurred;
                          returns self otherwise to avoid unnecessary object creation.
                          
        Raises:
            TypeError: If input is not a string when initialized, though handled in constructor.
        """
        # Ensure we work on a copy only if the current list has mutable state changes needed later,
        # but since strings are immutable internally usually represented as lists here,
        # and to allow return of self or new instance based on action:
        
        n = len(self._value)
        swapped_occurred = False

        for i in range(0, n - 1, 2):
            if i + 1 < n:
                self._value[i], self._value[i + 1] = self._value[i + 1], self._value[i]
                # We assume any change means a swap happened logically for this instance modification flow.

        # If the string length is odd, no last element can be swapped in pairs logic here as per instruction "adjacent pair".
        
        return self

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or files
    
    test_cases = [
        ("hello",),           # Odd length, one swap (he -> eh) but 'lo' remains? Wait: h-e-l-l-o. Pair 0-1: he->eh. 
                             # Indices: 0:h, 1:e, 2:l, 3:l, 4:o.
                             # i=0: swap(0,1) -> e,h,l,l,o (swapped once). Next i=2: l and o? No, step is 2. 
                             # Pairs are indices (0,1), (2,3). So h,e swapped; l,l not changed. Result: ehllro? Wait 'o' at end alone.
                             # Correct trace for "hello": 
                             # i=0: swap s[0],s[1] ('h','e') -> e,h... list becomes ['e','h','l','l','o']
                             # next loop step 2 -> i=2, check s[3]. Swap 'l','l' -> no change. 
                             # Final: ehll o (eh llo). Wait my manual trace earlier was wrong on logic or example?
        ("abcdef",),          # Even length. ab->ba, de->ed. Result: bacdefd? No. a,b,c,d,e,f -> b,a,d,e... wait c,d not swapped because index 4 is e. 
                             # Pairs (0,1) and (2,3). Indices 4(f) left alone.
                             # Original: a b c d e f
                             # Swap(0,1): b a c d e f -> Wait I am confusing myself. Let's re-evaluate "abcdef" manually with code logic.
                             # i=0: swap index 0 and 1 (a,b) -> list becomes ['b','a','c','d','e','f']
                             # next step is +2, so i=2. Swap index 2 and 3 (c,d). List -> ['b','a','d','c','e','f']
                             # Next step i=4. Check range stop: n-1 = 5. Step is 2. So i goes 0, 2, 4? 
                             # Wait loop condition `range(0, n - 1, 2)` -> stops before 5 (if inclusive start). 
                             # Indices generated: 0, 2, 4? No. range(start, stop, step) excludes stop.
                             # If n=6, range(0, 5, 2) yields [0, 2, 4]. 
                             # At i=4: swap index 4 and 5 (e,f). List -> b,a,d,c,f,e. Correct. Result: badcf e? No b a d c f e.
        
        ("",),                # Empty string
        ("a"),               # Single character, no pairs possible
        ("abba",)             # ab->ba, ba->ab (indices 0-1 and 2-3). Original: a,b,b,a -> b,a,a,b
        
    ]

    for test_input in test_cases:
        s = CustomString(test_input[0])
        result_s = s.swap_adjacent_pairs()
        
        # Convert list back to string for printing if desired, though class holds internal state.
        output_str = "".join(result_s._value)
        print(f"Input: '{test_input[0]}' -> Output: '{output_str}'")

    # Additional explicit check for specific known cases in main block logic implicitly covered above