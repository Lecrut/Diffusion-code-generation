import unittest

class TestStringReversal(unittest.TestCase):
    """Test cases for string reversal functionality."""

    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_character(self):
        result = reverse_string("a")
        self.assertEqual(result, "a")

    def test_two_characters(self):
        result = reverse_string("ab")
        self.assertEqual(result, "ba")

    def test_palindrome(self):
        result = reverse_string("radar")
        self.assertEqual(result, "radar")

    def test_mixed_case_letters(self):
        result = reverse_string("Hello World!")
        self.assertEqual(result, "!dlroW olleH",)

    def test_numbers_and_symbols(self):
        result = reverse_string("123!@#456")
        self.assertEqual(result, "654#@!321", )

def reverse_string(text: str) -> str:
    """Reverse the input string.

    Args:
        text (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user input or CLI args
    samples = [
        "",                       # Empty string
        "a",                      # Single character
        "Hello World!",          # Mixed case and punctuation
        "racecar",                # Palindrome
        "!@#$%",                  # Special characters only
        "Python 3.10",           # Spaces included
    ]

    print("Running manual tests with sample inputs:")
    for inp in samples:
        reversed_out = reverse_string(inp)
        expected = "".join(reversed(list(inp)))
        status = "PASS" if reversed_out == expected else "FAIL"
        print(f"Input: {inp!r} -> Output: {reversed_out!r} | Status: {status}")

    # Run the official test suite
    unittest.main(verbosity=2)