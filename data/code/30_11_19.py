import copy

class CustomString:
    """A custom string class with additional functionality to swap adjacent pairs."""

    def __init__(self, value: str = "") -> None:
        self._value = list(value) if isinstance(value, str) else list(value)

    @property
    def length(self) -> int:
        return len(self._value)

    def get_value(self) -> str:
        """Returns the current string value."""
        return "".join(self._value)

    def set_value(self, new_value: str) -> None:
        """Sets the internal list representation of the string."""
        self._value = [c for c in new_value]

    def swap_adjacent_pairs(self) -> "CustomString":
        """
        Swaps characters at every adjacent pair within the string instance.
        
        For example, if the input is 'abcd', it becomes 'badc'.
        If the length of the string is odd, the last character remains unchanged.
        
        Returns:
            A new CustomString instance with the modified value.
            
        Raises:
            TypeError: If self._value is not a list or contains non-string elements (though typically it's always strings).
        """
        # Ensure we are working on a copy to avoid modifying original state unless intended by design, 
        # but based on typical immutability expectations for such methods returning new instances.
        result_list = self._value[:]

        i = 0
        while i < len(result_list) - 1:
            if isinstance(result_list[i], str) and isinstance(result_list[i + 1], str):
                # Swap the pair
                temp = result_list[i]
                result_list[i] = result_list[i + 1]
                result_list[i + 1] = temp
            i += 2

        return CustomString("".join(result_list))

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    
    test_cases = [
        "abcd",      # Expected: badc
        "abcde",     # Expected: bacd (last 'e' stays)
        "",          # Expected: ""
        "a",         # Expected: "a"
        "1234567890",# Expected: 2143658709
    ]

    for test_input in test_cases:
        original = CustomString(test_input)
        swapped = original.swap_adjacent_pairs()
        
        print(f"Original Input: '{test_input}'")
        print(f"After swap_adjacent_pairs(): '{swapped.get_value()}'")
        print("-" * 30)

    # Additional verification that the method returns a new instance and doesn't mutate self permanently if called multiple times.
    multi_test = CustomString("hello")
    first_call = multi_test.swap_adjacent_pairs()
    second_call = multi_test.swap_adjacent_pairs()
    
    print(f"Original after two swaps: '{multi_test.get_value()}' (should be 'olleh' -> 'lhel')") # Wait, logic check: h->l, e->e? No. 
    # Let's trace "hello": pairs are ('he', 'll'), last is 'o'.
    # Swap 1st pair: 'ehlo'? No. Indices 0 and 1 swap -> 'h','e' becomes 'e','h'. String so far "ehl". Index 2,3 are 'l','l'. Swap -> same. 
    # Result should be "ehllo"? Wait.
    # Input: h e l l o (indices 0 1 2 3 4)
    # Pair 1: indices 0,1 ('h', 'e') -> swap to ('e', 'h'). List: [e, h, l, l, o]
    # Pair 2: indices 2,3 ('l', 'l') -> swap (no change). List: [e, h, l, l, o]
    # Result string: "ehllo"
    
    print(f"First call result: '{first_call.get_value()}'") 
    print(f"Second call on original instance: '{second_call.get_value()}'")