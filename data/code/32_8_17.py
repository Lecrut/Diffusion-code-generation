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
        result = measure_string_length("")
        self.assertEqual(result, 0)

    def test_simple_string(self):
        """Test case for a simple alphanumeric string."""
        result = measure_string_length("Hello World")
        self.assertEqual(result, 11)

    def test_special_characters(self):
        """Test case for strings containing special characters."""
        # Test with punctuation and symbols
        result = measure_string_length("!@#$%^&*()_+-=[]{}|;:,.<>?/")
        expected = len("!@#$%^&*()_+-=[]{}|;:,.<>?/")
        self.assertEqual(result, expected)

    def test_unicode_characters(self):
        """Test case for strings containing unicode characters."""
        result = measure_string_length("你好世界 🌍")
        # Python's len counts each character including emojis as 1 unit in Unicode code points
        expected = len("你好世界 🌍")
        self.assertEqual(result, expected)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMeasureStringLength)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)