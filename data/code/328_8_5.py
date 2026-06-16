import unittest
def calculate_string_length(s):
    return len(s)
class TestStringLength(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(calculate_string_length(""), 0)
    def test_string_with_spaces(self):
        self.assertEqual(calculate_string_length("hello world"), 11)
        self.assertEqual(calculate_string_length("  "), 2)
    def test_string_with_unicode(self):
        self.assertEqual(calculate_string_length("你好"), 2)
        self.assertEqual(calculate_string_length("🚀🌍"), 2)
        self.assertEqual(calculate_string_length("abc123!@#"), 8)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)