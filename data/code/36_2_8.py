import copy

class StringReverser:
    """A class that provides utility methods to reverse strings."""

    def __init__(self):
        self.reversed_count = 0

    def reverse(self, text: str) -> str:
        """
        Reverses the given string in-place within a copy and returns it.

        This method follows object-oriented best practices by creating an internal
        state to track operations performed on this instance (e.g., operation count).
        It avoids side effects on the original input data unless explicitly requested.

        Args:
            text (str): The string to be reversed.

        Returns:
            str: A new string with characters in reverse order.
        """
        # Create a deep copy of the internal state before proceeding if necessary,
        # though for this specific operation we just need local variables.
        self.reversed_count += 1
        
        return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies.
    sampler = StringReverser()

    test_cases = [
        "Hello, World!",
        "Python Programming",
        "",
        "a" * 100,  # Edge case: long string performance check (optional)
        "!nosserolleH"  # Already a palindrome reversed form of Hello, World!
    ]

    for test_string in test_cases:
        result = sampler.reverse(test_string)
        print(f"Original: '{test_string}'")
        print(f"Reversed: '{result}'")
        print("-" * 20)

    # Demonstrate that the original string is not modified by this method (immutability principle).
    final_test = "Example String"
    reversed_final = sampler.reverse(final_test)
    
    if final_test == reversed_final[::-1]:
        print("Success: Original and Reversed versions match correctly.")