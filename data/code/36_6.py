import unittest
class StringReverser:
    def reverse_string(self, s):
        return s[::-1]
class TestStringReverser(unittest.TestCase):
    def setUp(self):
        self.reverser = StringReverser()
    def test_reverse_empty_string(self):
        self.assertEqual(self.reverser.reverse_string(""), "")
    def test_reverse_simple_string(self):
        self.assertEqual(self.reverser.reverse_string("abc"), "cba")
    def test_reverse_palindrome(self):
        self.assertEqual(self.reverser.reverse_string("madam"), "madam")
    def test_reverse_with_spaces(self):
        self.assertEqual(self.reverser.reverse_string("hello world"), "dlrow olleh")
    def test_reverse_with_numbers(self):
        self.assertEqual(self.reverser.reverse_string("12345"), "54321")
    def test_reverse_with_mixed_case(self):
        self.assertEqual(self.reverser.reverse_string("Python"), "nohtyP")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)