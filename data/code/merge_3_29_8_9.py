import unittest

def reverse_string(s: str) -> str:
    """Reverse a given string."""
    return s[::-1]

class TestStringReversal(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_character(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_simple_reversible_word(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_palindrome(self):
        self.assertEqual(reverse_string("radar"), "radar")

    def test_uppercase_letters(self):
        self.assertEqual(reverse_string("Python"), "nohtyP")

    def test_with_spaces(self):
        self.assertEqual(reverse_string("Hello World"), "dlroW olleH")

    def test_special_characters_and_numbers(self):
        self.assertEqual(reverse_string("!1234567890-_-="), "=_-_0123456789!")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    samples = [
        ("", "empty string"),
        ("a", "single character"),
        ("hello world", "mixed case with spaces"),
        ("12345", "numbers only")
    ]

    print("Running manual test on sample values:")
    for input_str, description in samples:
        result = reverse_string(input_str)
        print(f"Input: '{input_str}' ({description}) -> Output: '{result}'")

    # Run the unit tests automatically if this file is executed as a script
    unittest.main(exit=False)