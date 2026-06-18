import unittest

def reverse_string(s: str) -> str:
    """Reverse a given string in-place logic applied to return a new reversed string."""
    return s[::-1]

class TestStringReversal(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_character(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_two_characters(self):
        self.assertEqual(reverse_string("ab"), "ba")

    def test_palindrome(self):
        self.assertEqual(reverse_string("radar"), "radar")

    def test_mixed_case_and_spaces(self):
        input_str = "Hello, World!"
        expected_output = "!dlroW ,olleH"
        self.assertEqual(reverse_string(input_str), expected_output)

    def test_special_characters(self):
        input_str = "@#$%^&*"
        expected_output = "*&^%$#@@"
        self.assertEqual(reverse_string(input_str), expected_output)

if __name__ == '__main__':
    # Hard-coded sample values for demonstration (not required by unittest runner but ensures no external deps)
    samples = [
        ("", ""),
        ("a", "a"),
        ("ab", "ba"),
        ("Hello World!", "!dlroW olleH"),
        ("12345", "54321")
    ]

    # Run the test suite with specific values if needed, but here we just run standard tests.
    # To demonstrate execution without input:
    unittest.main()