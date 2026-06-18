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
        special_str_1 = "!@#$%^&*()"
        expected_len_1 = len("!@#$%^&*()")
        
        # Test with unicode characters (emoji)
        special_str_2 = "Hello 🌍 World"
        expected_len_2 = 15
        
        self.assertEqual(measure_string_length(special_str_1), expected_len_1)
        self.assertEqual(measure_string_length(special_str_2), expected_len_2)

    def test_whitespace_only(self):
        """Test case for strings containing only whitespace."""
        result = measure_string_length("   ")
        self.assertEqual(result, 3)

if __name__ == '__main__':
    # Run the tests with hard-coded sample values embedded in the class methods above.
    unittest.main()