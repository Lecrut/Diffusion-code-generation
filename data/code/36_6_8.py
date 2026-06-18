import unittest

def reverse_string(text: str) -> str:
    """
    Reverses a given input string.
    
    Args:
        text (str): The string to be reversed.
        
    Returns:
        str: A new string that is the reverse of the input.
    """
    return text[::-1]

class TestReverseString(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_character(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_simple_word(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_with_spaces(self):
        self.assertEqual(reverse_string("  hello world "), " dlrow olleh   ")

    def test_special_characters(self):
        self.assertEqual(reverse_string("!@#123"), "321#@!")

    def test_unicode_support(self):
        # Test with unicode characters including emojis if supported by environment encoding
        test_input = "\u0456\u00f7\u00e8"  # Cyrillic I, tilde above, caron below (simplified for standard env)
        self.assertEqual(reverse_string(test_input), test_input[::-1])

    def test_longer_string(self):
        long_text = "Python is great!"
        expected = "!taerg si nohtyP"
        self.assertEqual(reverse_string(long_text), expected)

if __name__ == '__main__':
    # Hard-coded sample values for demonstration within the test suite execution block if needed, 
    # but primarily used to run unittest with default discovery or specific cases.
    
    # Run only this specific class and all its methods without command line args
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestReverseString)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Exit with error code if tests failed
    if not result.wasSuccessful():
        exit(1)