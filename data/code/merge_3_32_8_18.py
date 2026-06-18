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
        self.assertEqual(measure_string_length(""), 0)

    def test_normal_string(self):
        self.assertEqual(measure_string_length("Hello"), 5)

    def test_special_characters(self):
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        expected_len = len(special_chars)
        self.assertEqual(measure_string_length(special_chars), expected_len)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMeasureStringLength)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)