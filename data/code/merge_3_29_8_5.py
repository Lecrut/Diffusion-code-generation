import unittest

def reverse_string(s: str) -> str:
    """
    Reverses a given string.

    Parameters:
        s (str): The input string to be reversed.

    Returns:
        str: The reversed string.
    
    Examples:
        >>> reverse_string("hello")
        'olleh'
        >>> reverse_string("")
        ''
    """
    return s[::-1]

class TestReverseString(unittest.TestCase):
    def test_normal_case(self):
        self.assertEqual(reverse_string("Hello World"), "dlroW olleH")

    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_character(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_palindrome(self):
        self.assertEqual(reverse_string("radar"), "radar")

    def test_all_uppercase(self):
        self.assertEqual(reverse_string("TESTING"), "GNITSET")

if __name__ == '__main__':
    # Run the tests with sample cases included in unit tests, no user input required.
    suite = unittest.TestLoader().loadTestsFromTestCase(TestReverseString)
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    # Additional manual check for demonstration if preferred over running full test suite:
    print("\n--- Manual Sample Run ---")
    samples = ["hello", "", "a1b2c3", "Python"]
    for s in samples:
        reversed_s = reverse_string(s)
        status = "✓" if s == reversed_s[::-1] else "✗"
        print(f"{status} Input: '{s}' -> Output: '{reversed_s}' (Expected match)")

    # Exit with error code only if tests fail or manual check fails on known good input.
    result.wasSuccessful() and all(reverse_string(s) == s[::-1] for s in samples)