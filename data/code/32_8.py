import unittest
class TestStringLength(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(len(""), 0)
    def test_alphanumeric_string(self):
        self.assertEqual(len("hello"), 5)
    def test_string_with_spaces(self):
        self.assertEqual(len("hello world"), 11)
    def test_string_with_special_characters(self):
        self.assertEqual(len("!@#$%^&*()"), 10)
    def test_string_with_mixed_characters(self):
        self.assertEqual(len("a1b@c2"), 6)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)