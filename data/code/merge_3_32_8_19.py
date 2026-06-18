import unittest

def measure_string_length(s: str) -> int:
    """Returns an integer representing the length of a string."""
    return len(s)

class TestMeasureStringLength(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(measure_string_length(""), 0)

    def test_non_ascii_characters(self):
        special_chars = "😀🎉★☆❌✅"
        expected_length = len(special_chars)
        result = measure_string_length(special_chars)
        self.assertEqual(result, expected_length)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestMeasureStringLength)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)