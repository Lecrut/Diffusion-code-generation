import unittest

def reverse_string(s: str) -> str:
    """
    Reverses a given input string.
    
    Args:
        s (str): The string to be reversed.
        
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

    def test_multiple_words(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

    def test_special_characters_and_spaces(self):
        self.assertEqual(reverse_string("!@#$% "), "%$#@! ")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestReverseString)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)