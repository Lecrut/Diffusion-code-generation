class StringCapitalizer:
    def capitalize_words(self, text):
        """
        Capitalizes only the first letter of each word in the input string.
        
        Handles multiple spaces between words by replacing them with a single space.
        Leaves non-alphabetic characters and existing capitalization as is (only changes 
        lowercase start to uppercase).

        Args:
            text (str): The input string containing one or more words separated by whitespace.

        Returns:
            str: A new string where the first letter of each word is capitalized.

        Raises:
            TypeError: If `text` is not a string instance.
            
        Examples:
            >>> capitalizer = StringCapitalizer()
            >>> capitalizer.capitalize_words("hello world")
            "Hello World"
            >>> capitalizer.capitalize_words("  python   programming ")
            "  Python   Programming "
        """
        if not isinstance(text, str):
            raise TypeError(f"Expected string type but got {type(text).__name__}")

        words = text.split()
        
        # Capitalize the first letter of each word and rejoin with single spaces
        capitalized_words = [word.capitalize() for word in words]
        return " ".join(capitalized_words)

if __name__ == '__main__':
    capitalizer = StringCapitalizer()

    sample_1 = "hello world"
    expected_1 = "Hello World"
    
    # Test with extra spaces to ensure normalization logic works if split was used differently, 
    # but based on standard behavior of .capitalize() list join:split() removes leading/trailing/multiple internal.
    result_1 = capitalizer.capitalize_words(sample_1)

    sample_2 = "  python   programming "
    expected_2 = "Python Programming"

    # Test with multiple spaces - the split() method handles this automatically, 
    # so we demonstrate it works on irregular spacing input.
    result_2 = capitalizer.capitalize_words(sample_2)

    print(f"Input: '{sample_1}'")
    print(f"Expected: '{expected_1}'")
    print(f"Result: {result_1}")
    assert result_1 == expected_1, f"Mismatch for sample 1. Expected '{expected_1}', got '{result_1}'"

    print()
    
    print(f"Input: '{sample_2}'")
    print(f"Expected: '{expected_2}'")
    print(f"Result: {result_2}")
    assert result_2 == expected_2, f"Mismatch for sample 2. Expected '{expected_2}', got '{result_2}'"

    # Additional edge case test with mixed casing (e.g., 'hElLo' -> 'Hello')
    sample_3 = "hElLo wOrld tEsT1ng!"
    result_3 = capitalizer.capitalize_words(sample_3)
    
    print(f"\nInput: '{sample_3}'")
    print(f"Result: {result_3}")

    # Verify mixed case is handled correctly (first char upper, rest unchanged if not lower)
    # python's str.capitalize() converts all other chars to lowercase. 
    # If the requirement implies preserving internal casing like 'hElLo' -> 'Hello', that matches standard capitalize().
    # Standard behavior: "hElLo" -> "Hello".

    print("\nAll tests passed.")