import unittest

def measure_string_length(s: str) -> int:
    """
    Measures the length of a given string.
    
    Args:
        s (str): The input string to measure.
        
    Returns:
        int: The length of the string.
    """
    return len(s)

class TestMeasureStringLength(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(measure_string_length(""), 0)

    def test_single_character(self):
        self.assertEqual(measure_string_length("a"), 1)

    def test_normal_string(self):
        self.assertEqual(measure_string_length("hello world"), 11)

    def test_special_characters(self):
        special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        expected_len = len(special)
        actual_len = measure_string_length(special)
        self.assertEqual(actual_len, expected_len)

    def test_unicode_characters(self):
        unicode_str = "Hello 世界 🌍"
        self.assertEqual(measure_string_length(unicode_str), 14)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMeasureStringLength)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Exit with error code if tests failed (optional behavior based on standard practice, 
    # though not strictly forbidden by task constraints beyond "runnable")
    exit(result.wasSuccessful() and 0 or 1)