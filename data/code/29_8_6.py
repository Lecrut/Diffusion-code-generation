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

    def test_with_spaces(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

    def test_special_characters(self):
        self.assertEqual(reverse_string("!@#$%"), "%$#@!")

    def test_unicode_characters(self):
        self.assertEqual(reverse_string("你好世界"), "界世好你")

if __name__ == '__main__':
    # Hard-coded sample values for demonstration (no user input required)
    samples = [
        ("", ""),
        ("a", "a"),
        ("hello", "olleh"),
        ("Python is great!", "!taerg si nohtyP"),
        ("1234567890", "0987654321")
    ]

    # Run a quick manual check on samples before running the full test suite
    print("Running sample checks...")
    for input_str, expected in samples:
        result = reverse_string(input_str)
        assert result == expected, f"Failed for '{input_str}': got {result}, expected {expected}"
    print("All manual sample checks passed.")

    # Run the full unit test suite
    unittest.main(exit=False)  # exit=False keeps the process running after tests in some environments