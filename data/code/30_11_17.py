import sys

class CustomString:
    """A custom string class with methods to manipulate character sequences."""

    def __init__(self, value=""):
        self._value = list(value)  # Internal storage as a mutable list of characters

    def __str__(self):
        return "".join(self._value)

    def swap_adjacent_pairs(self):
        """Swaps the characters of every adjacent pair within the string instance.
        
        For example, "abcd" becomes "bacd", and "abcde" becomes "bcade".
        
        Edge cases:
            - Empty strings remain unchanged.
            - Strings with an odd number of characters swap pairs up to the last character (no-op for single char at end).

        Raises:
            TypeError: If value is not a string-like iterable of characters.
        """
        if not isinstance(self._value, list):
            raise TypeError("Internal state must be a list of characters.")

        # Iterate over the list in steps of 2 to avoid index errors on odd lengths
        for i in range(0, len(self._value), 2):
            j = i + 1
            if j < len(self._value):
                self._value[i], self._value[j] = self._value[j], self._value[i]

    def get_length(self) -> int:
        """Returns the length of the string."""
        return len(self._value)

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input
    
    test_cases = [
        "abcdef",      # Even length, full swapping -> "bacdef" is wrong logic check: a<->b, c<->d, e<->f => bacde? No. abcdfed? Let's trace: abcd ef g... 
                      # Input: 'a','b','c','d','e','f'
                      # Swap (0,1): b,a | Swap (2,3): d,c | Swap (4,5): f,e -> "badcf" + e+f? Wait.
                      # Original: a,b,c,d,e,f
                      # Pair 1: ab -> ba
                      # Pair 2: cd -> dc
                      # Pair 3: ef -> fe
                      # Result: badcfe
        "abcde",       # Odd length -> "bcade" (e stays)
        "",            # Empty string
        "x",           # Single character
        "!@#$%",       # Special chars mixed with letters
    ]

    print("Testing CustomString.swap_adjacent_pairs()")
    print("-" * 30)

    for test_val in test_cases:
        s = CustomString(test_val)
        original_str = str(s)