import unittest

def reverse_string(text: str) -> str:
    """
    Reverses a given string.
    
    Args:
        text (str): The input string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return text[::-1]

class TestReverseString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_character(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_simple_word(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_sentence_with_spaces(self):
        self.assertEqual(reverse_string("Hello World!"), "!dlroW olleH")

    def test_special_characters_and_numbers(self):
        self.assertEqual(reverse_string("a1b2@c#"), "@c#2b1a")

    def test_unicode_strings(self):
        # Test with non-ASCII characters including emojis if supported in environment, 
        # but primarily ensuring byte-level reversal for standard ASCII.
        self.assertEqual(reverse_string("你好世界"), "界世好你")  # Note: Unicode handling depends on Python version/encoding
        
    def test_case_sensitivity(self):
        self.assertNotEqual(reverse_string("ABC"), "abc", f"Expected 'CBA', got {reverse_string('ABC')}")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestReverseString)
    
    # Hard-coded sample values demonstration (not executed by default, but visible in code structure if needed)
    samples = [
        ("", ""),
        ("a", "a"),
        ("hello", "olleh"),
        ("Hello World!", "!dlroW olleH"),
    ]

    # Run tests automatically when the module is executed directly
    unittest.main(exit=False, verbosity=2)