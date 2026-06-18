import unittest

def reverse_string(text: str) -> str:
    """
    Reverses a given string in-place using slicing to create a new reversed string.
    
    Args:
        text (str): The input string to be reversed.
        
    Returns:
        str: A new string with characters in reverse order.
    """
    return text[::-1]

class TestReverseString(unittest.TestCase):

    def test_reverse_simple_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_reverse_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_reverse_single_character(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_reverse_number_sequence(self):
        self.assertEqual(reverse_string("12345"), "54321")

    def test_reverse_special_characters(self):
        self.assertEqual(reverse_string("!@#$%"), "%#$!@")

    def test_reverse_unicode_chars(self):
        self.assertEqual(reverse_string("你好世界"), '界世好你')

if __name__ == '__main__':
    # Sample execution without user input or external dependencies
    sample_input = "Reverse this string!"
    result = reverse_string(sample_input)
    print(f"Input: {sample_input}")
    print(f"Output: {result}")

    unittest.main()