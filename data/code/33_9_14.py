import unittest

def remove_spaces(input_string: str) -> str:
    """
    Removes all spaces from a given string.
    
    Args:
        input_string (str): The string to process.
        
    Returns:
        str: A new string with all spaces removed.
    """
    return input_string.replace(" ", "")

class TestRemoveSpaces(unittest.TestCase):
    """Test suite for the remove_spaces function."""

    def test_empty_string(self):
        self.assertEqual(remove_spaces(""), "", "Empty string should remain empty.")

    def test_only_spaces(self):
        self.assertEqual(remove_spaces("   "), "", "String with only spaces should become empty.")

    def test_no_spaces(self):
        self.assertEqual(remove_spaces("HelloWorld"), "HelloWorld", "String without spaces should be unchanged.")

    def test_mixed_characters_and_spaces(self):
        result = remove_spaces("The quick brown fox jumps over the lazy dog")
        expected = "Thequickbrownfoxjumpsoverthelazydog"
        self.assertEqual(result, expected)

    def test_multiple_consecutive_spaces(self):
        self.assertEqual(remove_spaces("a  b"), "ab", "Multiple consecutive spaces should be removed as a single removal.")

    def test_special_characters_preserved(self):
        result = remove_spaces("!@#$%^&*()")
        expected = "!@#$%^&*()"
        self.assertEqual(result, expected)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRemoveSpaces)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)