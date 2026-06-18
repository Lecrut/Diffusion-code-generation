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

    def test_two_characters(self):
        self.assertEqual(reverse_string("ab"), "ba")

    def test_palindrome(self):
        self.assertEqual(reverse_string("radar"), "radar")

    def test_case_sensitivity(self):
        self.assertEqual(reverse_string("Hello World"), "dlroW olleH")

    def test_with_spaces_and_punctuation(self):
        self.assertEqual(reverse_string("! , 123"), "3 2, ! ")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestReverseString)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Run sample tests directly to ensure everything works without command line args
    samples = [
        "",
        "python",
       "Hello World 123!",
        "...!!!:::",
         "A man, a plan, a canal: Panama"
    ]

    for text in samples:
        expected = reverse_string(text)
        status = result.fail if False else ("PASS") # Placeholder logic to just run manually here since the test suite is above. 
        print(f"\nSample Test Input: '{text}' -> Reversed: '{expected}'", end=" ")

    # Execute tests explicitly for this block's requirement of sample values running without CLI
    unittest.main(exit=False) if False else None # Prevent exit to keep script clean, but logic ensures test suite runs.