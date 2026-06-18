import unittest

def remove_spaces(text: str) -> str:
    """
    Removes all spaces from the input string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with all spaces removed.
    """
    return ''.join(char for char in text if not (' ' == char))

class TestRemoveSpaces(unittest.TestCase):
    """Test suite for the remove_spaces function."""

    def test_empty_string(self):
        self.assertEqual(remove_spaces(""), "")

    def test_only_spaces(self):
        self.assertEqual(remove_spaces("   "), "")

    def test_mixed_characters_with_spaces(self):
        input_str = "Hello World! This is a test."
        expected_output = "HelloWorld!Thisisatest"
        self.assertEqual(remove_spaces(input_str), expected_output)

    def test_no_spaces(self):
        self.assertEqual(remove_spaces("NoSpacesHere"), "NoSpacesHere")

    def test_single_space(self):
        self.assertEqual(remove_spaces("A B C"), "ABC")

    def test_multiple_consecutive_spaces(self):
        self.assertEqual(remove_spaces("A   B  C"), "AB C")

if __name__ == '__main__':
    # Hard-coded sample values for demonstration (not used in actual assertions)
    SAMPLE_CASES = [
        ("", ""),
        ("   ", ""),
        ("Hello World!", "HelloWorld!"),
        ("NoSpacesHere", "NoSpacesHere"),
        ("A B C", "ABC"),
        ("  Multiple   Spaces  Here  ", "MultipleSpacesHere")
    ]

    # Run the unit tests if executed directly
    unittest.main()