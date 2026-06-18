class StringManipulator:
    """A class providing optimized string manipulation methods."""

    def to_lowercase(self, text: str) -> str:
        """Converts a given string to lowercase using built-in method."""
        return text.lower()

    def to_uppercase(self, text: str) -> str:
        """Converts a given string to uppercase using built-in method."""
        return text.upper()

    def to_title_case(self, text: str) -> str:
        """Converts a given string to title case (first letter of each word capitalized)."""
        # Using capitalize on split and join is often more efficient than translate for complex cases,
        # but standard .title() handles most requirements. We use the built-in .title().
        return text.title()

    def swap_case(self, text: str) -> str:
        """Swaps case of all characters in a string using built-in method."""
        return text.swapcase()

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    test_string = "Hello World! This is A Test String."

    manipulator = StringManipulator()

    result_lower = manipulator.to_lowercase(test_string)
    print(f"Lowercase: {result_lower}")

    result_upper = manipulator.to_uppercase(test_string)
    print(f"Uppercase: {result_upper}")

    result_title = manipulator.to_title_case(test_string)
    print(f"Title Case: {result_title}")

    result_swap = manipulator.swap_case(test_string)
    print(f"Swap Case: {result_swap}")