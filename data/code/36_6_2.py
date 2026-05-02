import unittest
class StringReverser:
    def reverse_string(self, s):
        return s[::-1]
class TestStringReverser(unittest.TestCase):
    def setUp(self):
        self.reverser = StringReverser()
    def test_empty_string(self):
        self.assertEqual(self.reverser.reverse_string(""), "")
    def test_simple_string(self):
        self.assertEqual(self.reverser.reverse_string("abc"), "cba")
    def test_palindrome(self):
        self.assertEqual(self.reverser.reverse_string("madam"), "madam")
    def test_with_spaces(self):
        self.assertEqual(self.reverser.reverse_string("hello world"), "dlrow olleh")
    def test_with_numbers_and_symbols(self):
        self.assertEqual(self.reverser.reverse_string("123!@#"), "#@!321")
    def test_long_string(self):
        self.assertEqual(self.reverser.reverse_string("abcdefghij"), "jihgfedcba")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)