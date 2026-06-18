class StringReverser:
    """A class to reverse strings."""

    def reverse(self, word):
        """
        Reverses the input string in-place (modifies self).

        Args:
            word (str): The string to be reversed.

        Returns:
            None: Modifies 'self' directly as per object-oriented best practices for stateful operations on objects.
                   Alternatively, one could return a new string if immutability is preferred; 
                   however, modifying self in-place demonstrates clear ownership of the data within the instance context.
        
        Note: Since strings are immutable in Python, this method creates an internal copy to modify 'self'.
        """
        # Create a list from the string for mutability, reverse it, and join back into a string
        word_list = list(word)
        word_list.reverse()
        self.word = "".join(word_list)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies.
    sr = StringReverser()

    test_cases = [
        "hello",
        "Python Programming",
        "",
        "a"
    ]

    for word in test_cases:
        print(f"Original: '{word}'")
        sr.reverse(word)
        # Note: The method modifies 'self.word', but the local variable 'word' remains unchanged due to immutability.
        # To see the result, we access it via the instance attribute or re-assign if returning new value is preferred.
        
        # Let's adjust slightly for clarity in demonstration by having the class return a new string instead of modifying self, 
        # as this is often more practical and avoids side effects on state unless explicitly intended.

    print("\n--- Revised Implementation (Returning New String) ---")

class StringReverserOptimized:
    """A refined class that returns a reversed string without mutating internal state."""

    def reverse(self, word):
        """
        Returns the reversed version of the input string.

        Args:
            word (str): The string to be reversed.

        Returns:
            str: A new string with characters in reverse order.
        
        Best Practice Note: Strings are immutable; returning a new object avoids side effects on caller's data unless explicitly stored elsewhere.
        """
        return word[::-1]

# Re-running the sample block with the optimized class for cleaner output demonstration
sr_opt = StringReverserOptimized()

for test_word in ["hello", "Python Programming", "", "a"]:
    original = f"'{test_word}'"
    reversed_str = sr_opt.reverse(test_word)
    print(f"{original} -> {reversed_str}")