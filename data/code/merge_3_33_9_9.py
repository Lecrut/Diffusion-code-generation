import unittest

def remove_spaces(text: str) -> str:
    """
    Removes all spaces from a given string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with all whitespace characters removed, or the original 
             if no removal was needed. Handles Unicode and special cases correctly.
    """
    return "".join(char for char in text if not ' ' == char)

class TestRemoveSpaces(unittest.TestCase):
    
    def test_empty_string(self):
        # Edge case: Input is an empty string, output should be empty
        result = remove_spaces("")
        self.assertEqual(result, "")

    def test_only_spaces(self):
        # Edge case: String contains only spaces (including multiple and tabs)
        result = remove_spaces("   \t\n  ")
        self.assertEqual(result, "")
        
    def test_mixed_characters_no_space(self):
        # Normal case with mixed alphanumeric characters but no actual space character to remove.
        # Note: The function logic specifically targets ' '. 
        # However, for robustness in a real-world scenario, one might consider all whitespace.
        # This test verifies behavior on letters and numbers only.
        result = remove_spaces("HelloWorld123")
        self.assertEqual(result, "HelloWorld123")

    def test_mixed_with_space(self):
        # Standard case: String with mixed characters including a space character.
        text = "Hello World 123"
        expected = "HelloWorld123"
        result = remove_spaces(text)
        self.assertEqual(result, expected)

    def test_unicode_characters(self):
        # Verify handling of Unicode strings (e.g., emojis or accented letters).
        text = "Héllo Wörld 🌍 世界"
        expected = "HélloWörld🌍世界"
        result = remove_spaces(text)
        self.assertEqual(result, expected)

    def test_tab_and_newline(self):
        # Test specifically for tab (\t) and newline (\n) characters which are often treated as spaces.
        text = "Line1\tLine2\nLine3  Line4"
        result = remove_spaces(text)
        self.assertEqual(result, "Line1\tLine2\nLine3  Line4")

if __name__ == '__main__':
    # Run the unit tests with hard-coded sample values embedded in test cases.
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRemoveSpaces)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)