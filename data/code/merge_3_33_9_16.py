import unittest

def remove_spaces(text: str) -> str:
    """
    Removes all spaces from a given string.
    
    Args:
        text (str): The input string potentially containing spaces.
        
    Returns:
        str: A new string with no spaces, same length otherwise.
    """
    return "".join(char for char in text if not (" " == char))

class TestRemoveSpaces(unittest.TestCase):

    def test_empty_string(self):
        """Test case where the input is an empty string."""
        self.assertEqual(remove_spaces(""), "")

    def test_only_spaces(self):
        """Test case where the input contains only spaces."""
        self.assertEqual(remove_spaces("     "), "")
        self.assertEqual(remove_spaces("\t\n\r  \n"), "\t\n\r")  # Non-space whitespace preserved as per logic, but typically "all spaces" implies ' '. 
        # Re-evaluating requirement: usually "remove all spaces" means the space character ' ', not tabs/newlines.
        # However, to be strict on "spaces", we only remove ASCII 32 (space).
        self.assertEqual(remove_spaces("   "), "")

    def test_mixed_characters(self):
        """Test case with a mix of letters, numbers, punctuation, and spaces."""
        input_str = "Hello World! This is a Test."
        expected_output = "HelloWorld!ThisisaTest."
        self.assertEqual(remove_spaces(input_str), expected_output)

    def test_multiple_consecutive_spaces(self):
        """Test case with multiple consecutive space characters."""
        self.assertEqual(remove_spaces("A  B   C"), "ABC")

    def test_unicode_characters_with_space(self):
        """Test case ensuring unicode letters are preserved while removing ASCII spaces."""
        input_str = "Héllo Wörld"
        expected_output = "HélloWörld"
        self.assertEqual(remove_spaces(input_str), expected_output)

if __name__ == '__main__':
    # Run the test suite with hardcoded sample values implicitly covered by methods.
    # Creating a custom runner to print results if desired, though standard unittest is sufficient.
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRemoveSpaces)
    
    # Run tests directly without command line args or input prompts
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    # Exit with appropriate code based on test results (for script execution context)
    import sys
    if not result.wasSuccessful():
        sys.exit(1)