import unittest

def measure_string_length(s: str) -> int:
    """Returns the length of the input string."""
    return len(s)

class TestMeasureStringLength(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(measure_string_length(""), 0)

    def test_normal_string(self):
        result = measure_string_length("Hello, World!")
        self.assertEqual(result, 13)

    def test_special_characters(self):
        special_str = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
        expected_len = len(special_str)
        actual_len = measure_string_length(special_str)
        self.assertEqual(actual_len, expected_len)

if __name__ == '__main__':
    pass
