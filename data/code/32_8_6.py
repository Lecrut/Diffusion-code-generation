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
        """Test case for strings containing special characters like punctuation and symbols."""
        # Test with mixed special characters including newlines if applicable (though len handles them as chars)
        result = measure_string_length("!@#$%^&*()_+-=[]{}|;':,./<>?")
        self.assertEqual(result, 23)

    def test_unicode_characters(self):
        """Test case for strings containing unicode characters."""
        # Using a string with emojis and accented letters
        result = measure_string_length("Hello 🌍! Café")
        self.assertEqual(result, 14)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMeasureStringLength)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)