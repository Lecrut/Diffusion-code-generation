import unittest

def reverse_string(s: str) -> str:
    """
    Reverses a given string in-place conceptually but returns a new string.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: A new string that is the reverse of the input string.
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

    def test_unicode_characters(self):
        self.assertEqual(reverse_string("你好，世界！"), "界世，好你！")

if __name__ == '__main__':
    # Hard-coded sample values for demonstration (not interactive)
    samples = [
        ("", ""),
        ("a", "a"),
        ("ab", "ba"),
        ("Hello, World!", "!dlroW ,olleH"),
        ("你好，世界！", "界世，好你！")
    ]

    # Run the module's unit tests with verbose output for clarity
    unittest.main(argv=[''], verbosity=2)