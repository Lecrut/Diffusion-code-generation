import string

class StringAssembler:
    def __init__(self):
        """Initialize an empty assembler."""
        pass

    def build(self, parts, separator=''):
        """
        Efficiently constructs a new string from the input list of parts and a chosen separator.

        Args:
            parts (list[str]): A list of strings to be joined.
            separator (str): The string that separates each part in the final result. Default is empty string.

        Returns:
            str: The constructed string.
        """
        if not isinstance(parts, list) or any(not isinstance(p, str) for p in parts):
            raise TypeError("parts must be a list of strings")
        
        # Using join method which is highly optimized internally (typically C implementation)
        return separator.join(parts)

if __name__ == '__main__':
    assembler = StringAssembler()

    sample_parts = ["Hello", "World"]
    sample_separator = "!"

    result = assembler.build(sample_parts, sample_separator)

    print(f"Joined string: {result}")

    # Additional test case with default separator (empty string)
    parts_with_spaces = ["Python", "is", "great"]
    result_default = assembler.build(parts_with_spaces)

    print(f"Joined string (default): {result_default}")

    # Test case with multiple separators in list to ensure robustness
    mixed_parts = [1, 2]
    try:
        assembler.build(mixed_parts, ",")
    except TypeError as e:
        print(f"Expected error occurred for non-string parts: {e}")