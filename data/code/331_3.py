import unittest
def lowercase_converter(input_string):
    return input_string.lower()
class TestLowercaseConverter(unittest.TestCase):
    def test_lowercase_basic(self):
        self.assertEqual(lowercase_converter("Hello"), "hello")
    def test_lowercase_already_lower(self):
        self.assertEqual(lowercase_converter("world"), "world")
    def test_lowercase_mixed_case(self):
        self.assertEqual(lowercase_converter("MiXeD CaSe"), "mixed case")
    def test_lowercase_empty_string(self):
        self.assertEqual(lowercase_converter(""), "")
    def test_lowercase_numbers_and_symbols(self):
        self.assertEqual(lowercase_converter("Test123!"), "test123!")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)