import unittest

def measure_string_length(s: str) -> int:
    """
    Measures the length of a given string.
    
    Parameters:
        s (str): The input string to measure.
        
    Returns:
        int: The number of characters in the string.
    """
    return len(s)

class TestMeasureStringLength(unittest.TestCase):

    def test_empty_string(self):
        """Test case for an empty string."""
        self.assertEqual(measure_string_length(""), 0)

    def test_single_character(self):
        """Test case for a single character string."""
        result = measure_string_length("a")
        self.assertEqual(result, 1)

    def test_special_characters_unicode(self):
        """Test case for strings containing special characters and Unicode symbols."""
        unicode_str = "Hello! @#$%^&*()_+-=[]{}|;':\",./<>?" + "\u2603\u274C"
        expected_length = len(unicode_str)
        self.assertEqual(measure_string_length(unicode_str), expected_length)

    def test_whitespace_and_tabs(self):
        """Test case for strings with whitespace and tab characters."""
        ws_str = "  \t\n\r   "
        expected_length = len(ws_str)
        self.assertEqual(measure_string_length(ws_str), expected_length)

if __name__ == '__main__':
    # Run the unit tests directly to verify functionality without user input or external dependencies.
    unittest.main(exit=False, verbosity=2)