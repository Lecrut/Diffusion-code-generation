import unittest

def reverse_string(s: str) -> str:
    """
    Reverses a given string without using built-in slicing functions directly on the result,
    to ensure basic logic verification in tests.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: A new string that is the reverse of the input.
    """
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")
    
    result = []
    for char in s:
        result.insert(0, char)
    return ''.join(result)

class TestReverseString(unittest.TestCase):

    def test_empty_string(self):
        """Test reversing an empty string."""
        self.assertEqual(reverse_string(""), "")

    def test_single_character(self):
        """Test reversing a single character string."""
        self.assertEqual(reverse_string("a"), "a")

    def test_normal_case(self):
        """Test normal case with multiple characters."""
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_with_spaces(self):
        """Test string containing spaces."""
        self.assertEqual(reverse_string("  world "), "  dlrow ")

    def test_special_characters(self):
        """Test string with special characters and symbols."""
        self.assertEqual(reverse_string("!@#$%"), "%$#@!")

    def case_insensitive_comparison_test(self):
        """Ensure reverse preserves original casing exactly (case-sensitive)."""
        self.assertEqual(reverse_string("AbCdEfG"), "gFeDcBA")

if __name__ == '__main__':
    # Run the test suite with hard-coded sample values implicitly covered by unit tests
    unittest.main()