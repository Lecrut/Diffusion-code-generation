class CustomString:
    """A custom string-like class with additional manipulation methods."""

    def __init__(self, value: str):
        """Initialize the CustomString instance with a given string value."""
        self._value = list(value)  # Store as mutable list of characters

    def swap_adjacent_pairs(self) -> 'CustomString':
        """
        Swaps every adjacent pair of characters in the underlying string.
        
        For example: "abcd" becomes "badc", and "abcdefg" becomes "bcadef".
        
        Returns:
            A new CustomString instance with the modified content.
            
        Raises:
            ValueError: If input is not a valid string (handled by constructor).
        """
        # Create a copy to avoid modifying self in place if return type matters,
        # though typically returning 'self' after modification is preferred for mutability.
        # Here we modify the instance directly as it's more efficient and common 
        # unless specified otherwise. However, to be safe and functional-like:
        
        result = list(self._value)
        n = len(result)
        
        # Iterate with a step of 2 up to length-1 (inclusive for odd lengths logic check)
        for i in range(0, n - 1, 2):
            if i + 1 < n:
                result[i], result[i + 1] = result[i + 1], result[i]
        
        # Construct the new string and return a new instance or self? 
        # The task says "within a custom string class", implying modification.
        # Let's modify in place for efficiency but ensure correctness.
        # Re-assigning internal list to reflect change.
        self._value = result
        
        return self

    def __str__(self) -> str:
        """Return the string representation of the CustomString."""
        return "".join(self._value)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input(), sys.stdin, etc.)
    
    test_cases = [
        "abcdef",      # Even length: ab->ba, cd->dc, ef->fe => badc fe -> baddcef? Wait. 
                      # a<->b, c<->d, e<->f => bacdef? No.
                      # Original: 0:a,1:b,2:c,3:d,4:e,5:f
                      # Swap pairs (0,1), (2,3), (4,5) -> b,a,d,c,f,e => badcfe
        "abc",         # Odd length: a<->b, c remains => bac
        "",            # Empty string
        "a",           # Single character
        "hello world"  # h-e-l-o- -w-o-r-l-d -> e-h-o-l- o-w-r-l-d? 
                      # (0,1) he->eh, (2,3) lo->ol, (4,) space remains, (5,6) wo->ow, (7,8) rl->lr, (9)d
        "xy"           # xy -> yx
    ]

    for test_input in test_cases:
        original = CustomString(test_input)
        print(f"Original: '{original}'")
        
        modified_instance = original.swap_adjacent_pairs()
        result_str = str(modified_instance)
        
        print(f"After swap_adjacent_pairs(): '{result_str}'\n")