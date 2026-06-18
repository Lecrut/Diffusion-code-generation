import sys

class CustomString:
    """A custom string class with a method to swap adjacent character pairs."""

    def __init__(self, value: str = "") -> None:
        self._value = list(value)

    def __str__(self) -> str:
        return "".join(self._value)

    def swap_adjacent_pairs(self) -> "CustomString":
        """
        Swaps the characters of every adjacent pair within the string instance.
        
        The method modifies the internal representation in-place and returns 
        a new CustomString object containing the modified value to allow for 
        immutability semantics similar to built-in strings, while also providing 
        access to the original class structure if needed.

        Edge cases handled:
            - Empty string or single character: Returns unchanged instance.
            - Odd length string: The last unpaired character remains in place.

        Args:
            None (modifies self internally and returns a new object)

        Returns:
            CustomString: A new instance with swapped adjacent pairs.
        """
        # Create a copy to avoid modifying the original if intended as immutable behavior,
        # though typically 'in-place' modification is implied by "within the string instance".
        # Given the requirement for robustness and clean design, we return a new object 
        # containing the modified state. If in-place mutation was strictly required without 
        # returning a copy, self._value could be mutated directly before assignment logic below.
        
        result = list(self._value)
        n = len(result)

        for i in range(0, n - 1, 2):
            if i + 1 < n:
                result[i], result[i + 1] = result[i + 1], result[i]

        return CustomString("".join(result))

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    
    test_cases = [
        "abcdef",      # Even length, full swaps: fedcba -> bacdef (wait logic check) 
                      # Input: a b c d e f -> Swap(a,b), (c,d), (e,f) -> b a d c f e
        "abc",         # Odd length, last char stays: ba c
        "",            # Empty string
        "a",           # Single character
        "1234567890"  # Digits example
    ]

    for test_input in test_cases:
        original = CustomString(test_input)
        swapped = original.swap_adjacent_pairs()
        
        print(f"Original Input: '{test_input}'")
        print(f"After swap_adjacent_pairs(): '{swapped}'")
        print("-" * 30)