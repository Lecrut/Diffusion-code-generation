import unittest

def measure_string_length(s: str) -> int:
    """
    Measures the length of a given string.
    
    Args:
        s (str): The input string whose length is to be measured.
        
    Returns:
        int: The number of characters in the string.
    """
    return len(s)

class TestMeasureStringLength(unittest.TestCase):
    def test_empty_string(self):
        """Test case for an empty string."""
        self.assertEqual(measure_string_length(""), 0)

    def test_simple_ascii_string(self):
        """Test case for a simple ASCII string."""
        self.assertEqual(measure_string_length("Hello"), 5)

    def test_unicode_characters(self):
        """Test case for strings with Unicode characters including emojis and Chinese chars."""
        unicode_str = "你好世界 🌍"
        # Length should be correct in Python's len() function which counts code points/characters as expected by standard string length definition.
        self.assertEqual(measure_string_length(unicode_str), 9)

    def test_special_characters(self):
        """Test case for strings containing special symbols."""
        special_str = "!@#$%^&*()"
        self.assertEqual(measure_string_length(special_str), len("!@#$%^&*()"))

if __name__ == '__main__':
    # Run the unit tests with hard-coded sample values verified within test methods above.
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMeasureStringLength)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Exit with error code if any tests failed
    exit(result.wasSuccessful() and 0 or 1)