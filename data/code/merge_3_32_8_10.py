import unittest

def measure_string_length(s: str) -> int:
    """
    Measures the length of a given string.
    
    Args:
        s (str): The input string to measure.
        
    Returns:
        int: The number of characters in the string.
    """
    return len(s)

class TestMeasureStringLength(unittest.TestCase):

    def test_empty_string(self):
        """Test case for an empty string."""
        self.assertEqual(measure_string_length(""), 0)

    def test_normal_string(self):
        """Test case for a normal alphanumeric string."""
        result = measure_string_length("Hello World")
        self.assertEqual(result, 11)

    def test_special_characters(self):
        """Test case for strings containing special characters."""
        # Test with punctuation and symbols
        s_with_punctuation = "Hello! @#$%^&*()"
        expected_len = len(s_with_punctuation)
        self.assertEqual(measure_string_length(s_with_punctuation), expected_len)

    def test_unicode_characters(self):
        """Test case for strings containing unicode characters."""
        # Test with emoji and non-ASCII letters
        s_emoji = "Hello 🌍 World"
        result = measure_string_length(s_emoji)
        self.assertEqual(result, len(s_emoji))

    def test_single_character(self):
        """Test case for a string containing only one character."""
        self.assertEqual(measure_string_length("a"), 1)

if __name__ == '__main__':
    # Hard-coded sample values and execution without user input or external dependencies
    
    if __name__ == "__main__":
        unittest.main()