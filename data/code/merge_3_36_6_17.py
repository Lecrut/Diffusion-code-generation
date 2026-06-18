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

    def test_normal_case(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

    def test_with_spaces_and_punctuation(self):
        self.assertEqual(reverse_string("! , 123"), "321 ! ,")

    def test_unicode_characters(self):
        self.assertEqual(reverse_string("你好世界"), "界世好你")

if __name__ == '__main__':
    pass
