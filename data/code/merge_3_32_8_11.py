import unittest

def measure_string_length(s: str) -> int:
    """
    Measures the length of a given string by counting its characters.
    
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
        result = measure_string_length("Hello")
        self.assertEqual(result, 5)

    def test_special_characters(self):
        """Test case for strings containing special characters like spaces and symbols."""
        result = measure_string_length("!@#$%^&*()_+-=[]{}|;:,.<>?/")
        expected = len("!@#$%^&*()_+-=[]{}|;:,.<>/?")
        self.assertEqual(result, expected)

    def test_unicode_characters(self):
        """Test case for strings containing unicode characters."""
        result = measure_string_length("Hello 世界 🌍")
        # '🌍' is a single character but takes multiple bytes in UTF-8; len() counts it as one.
        expected = 12
        self.assertEqual(result, expected)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMeasureStringLength)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)