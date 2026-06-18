import unittest

def remove_all_spaces(text: str) -> str:
    """
    Removes all spaces from the input string.
    
    Args:
        text (str): The input string potentially containing spaces.
        
    Returns:
        str: A new string with all spaces removed.
    """
    return ''.join(char for char in text if not (' ' == char))

class TestRemoveAllSpaces(unittest.TestCase):
    """Test suite for the remove_all_spaces function."""

    def test_empty_string(self):
        """Tests behavior when input is an empty string."""
        result = remove_all_spaces("")
        self.assertEqual(result, "")

    def test_only_spaces(self):
        """Tests behavior when input contains only spaces."""
        inputs_with_spaces = ["   ", "\t\n", "  \n\t "]
        expected_results = ["" , "", ""]
        
        for i in range(len(inputs_with_spaces)):
            result = remove_all_spaces(inputs_with_spaces[i])
            self.assertEqual(result, expected_results[i], 
                             f"Failed for input '{inputs_with_spaces[i]}'")

    def test_mixed_characters(self):
        """Tests behavior with strings containing mixed alphanumeric characters and spaces."""
        inputs_and_expected = [
            ("Hello World", "HelloWorld"),
            ("  Leading Spaces ", "LeadingSpaces "),
            ("Trailing   Spaces", "TrailingSpaces"),
            ("Multiple\t\nNewlines\rand Spaces", "MultipleNewlandSpaces"),
            ("a b c d e f g h i j k l m n o p q r s t u v w x y z ", 
             "abcdefghijklmnopqrstuvwxyz "),
        ]

        for input_str, expected_output in inputs_and_expected:
            with self.subTest(input=input_str):
                result = remove_all_spaces(input_str)
                self.assertEqual(result, expected_output)

if __name__ == '__main__':
    # Hard-coded sample values to run the tests without user input or external dependencies.
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRemoveAllSpaces)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    if not result.wasSuccessful():
        exit(result.failures[0][1] if result.failures else result.errors[0][1])