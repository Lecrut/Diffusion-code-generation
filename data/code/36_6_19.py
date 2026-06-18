import unittest

def reverse_string(s: str) -> str:
    """
    Reverses a given string in place without modifying the original input, 
    by constructing a new reversed version using slicing. This approach is efficient and readable.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: A new string that is the reverse of the input.
    """
    return s[::-1]

class TestReverseString(unittest.TestCase):
    """Unit tests for the reverse_string function."""

    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_character(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_two_characters(self):
        self.assertEqual(reverse_string("ab"), "ba")

    def test_palindrome(self):
        self.assertEqual(reverse_string("radar"), "radar")

    def test_case_sensitivity_preservation(self):
        self.assertEqual(reverse_string("Hello World"), "dlroW olleH")

    def test_special_characters_and_spaces(self):
        self.assertEqual(reverse_string("!@# "), "#!@ ")

    def test_unicode_support(self):
        # Test with Unicode characters including CJK and emoji (if supported in environment)
        self.assertEqual(reverse_string("你好世界"), "界世好你")

class SampleBlock:
    """Contains sample values for manual testing when the module is run directly."""
    
    @staticmethod
    def run_samples():
        samples = [
            ("", ""),
            ("a", "a"),
            ("ab", "ba"),
            ("Hello World!", "!dlroW olleH"),
            ("1234567890", "0987654321"),
        ]

        print("Running sample tests...")
        for input_str, expected in samples:
            result = reverse_string(input_str)
            status = "PASS" if result == expected else f"FAIL (Expected '{expected}', got '{result}')"
            print(f"'{input_str}' -> {status}")

if __name__ == '__main__':
    # Run the sample block for immediate verification without command-line arguments or input prompts
    SampleBlock.run_samples()

    # Execute unit tests with verbose output to see which cases pass/fail and their details
    unittest.main(verbosity=2)