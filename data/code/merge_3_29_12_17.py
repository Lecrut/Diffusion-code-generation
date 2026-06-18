class StringReverser:
    """A class designed to reverse strings efficiently."""

    def __init__(self, input_string: str = None):
        """Initialize with an optional string. If not provided, initializes as empty string."""
        self._string_input = input_string if input_string is not None else ""

    @property
    def original(self) -> str:
        """Returns the original string stored in this object."""
        return self._string_input

    def reverse(self) -> str:
        """Efficiently reverses and returns a new string. Modifies nothing internally to maintain immutability principle of strings."""
        # Python's slicing with step -1 is highly optimized at the C level, 
        # making it one of the most efficient ways to create a reversed copy in pure Python.
        return self._string_input[::-1]

if __name__ == '__main__':
    # Sample values hard-coded as per requirements (no user input or files)

    test_cases = [
        "Hello, World!",
        "",
        "A",
        "Python is awesome.",
        "To be or not to be"
    ]

    print("String Reverser Test Results")
    print("-" * 30)

    for original in test_cases:
        reverser = StringReverser(original=original)
        reversed_result = reverser.reverse()
        
        # Verification check (optional but demonstrates correctness)
        assert reversed_result == original[::-1], "Internal logic failed"

        print(f"Original: {repr(original)}")
        print(f"Reversed:{repr(reversed_result)}")
        print("-" * 30)