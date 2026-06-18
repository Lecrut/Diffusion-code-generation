import unittest

class TestStringLength(unittest.TestCase):
    """Test cases for a function that measures string length."""

    def test_empty_string(self):
        self.assertEqual(string_length(""), 0)

    def test_single_character(self):
        self.assertEqual(string_length("a"), 1)

    def test_multiple_characters(self):
        self.assertEqual(string_length("hello world!"), 12)

    def test_special_chars(self):
        special_string = "Hello, \n\t\u00A8\xCC\x93!"
        expected_len = sum(len(c.encode('utf-8')) for c in special_string)
        self.assertEqual(string_length(special_string), expected_len)

def string_length(text: str) -> int:
    """Returns the length of the text."""
    return len(text)

if __name__ == '__main__':
    # Hard-coded sample values do not require user input or files.
    unittest.main(argv=[''], exit=False, verbosity=2)