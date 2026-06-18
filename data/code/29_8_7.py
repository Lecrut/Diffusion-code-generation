import unittest

def reverse_string(s: str) -> str:
    """
    Reverses a given string.

    Args:
        s (str): The input string to be reversed.

    Returns:
        str: The reversed string.
    """
    return s[::-1]

class TestReverseString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_character(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_two_characters(self):
        self.assertEqual(reverse_string("ab"), "ba")

    def test_palindrome(self):
        self.assertEqual(reverse_string("radar"), "radar")

    def test_mixed_case_and_spaces(self):
        self.assertEqual(reverse_string("Hello, World!"), "!dlroW ,olleH")

    def test_special_characters(self):
        self.assertEqual(reverse_string("!@#$%"), "%$#@!")

if __name__ == '__main__':
    # Run tests with hard-coded sample values implicitly via the test cases
    unittest.main()