import unittest
class TestStringLength:
    def test_string_length(self):
        self.assertEqual(len("hello"), 5)
        self.assertEqual(len(""), 0)
        self.assertEqual(len("abcde"), 5)
        self.assertEqual(len("!@#$%^&*()"), 10)
        self.assertEqual(len("a"), 1)
        self.assertEqual(len("long string with spaces"), 22)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)