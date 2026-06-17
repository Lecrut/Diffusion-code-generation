import unittest
class TestStringConverter(unittest.TestCase):
    def test_lowercase_converter(self):
        self.assertEqual(lowercase_converter("Hello"), "hello")
        self.assertEqual(lowercase_converter("WORLD"), "world")
        self.assertEqual(lowercase_converter("Python 3.10"), "python 3.10")
        self.assertEqual(lowercase_converter("ALLCAPS"), "allcaps")
        self.assertEqual(lowercase_converter(""), "")
        self.assertEqual(lowercase_converter("aBcDeFg"), "abcdefg")
def lowercase_converter(input_string):
    return input_string.lower()
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)