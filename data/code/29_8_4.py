import unittest

def reverse_string(s: str) -> str:
    """
    Reverse a given string.
    
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

    def test_two_characters(self):
        self.assertEqual(reverse_string("ab"), "ba")

    def test_palindrome(self):
        self.assertEqual(reverse_string("racecar"), "racecar")

    def test_mixed_case_and_spaces(self):
        self.assertEqual(reverse_string("Hello, World!"), "!dlroW ,olleH")

    def test_special_characters(self):
        self.assertEqual(reverse_string("!@#%^&*()"), "()*&^%#@!")

if __name__ == '__main__':
    # Sample execution without user input or command-line arguments
    sample_cases = [
        ("", "empty string"),
        ("abc123", "digits and letters"),
        ("Python is great!", "mixed content with punctuation"),
        ("Madam", "palindrome test")
    ]

    # Run the function on samples to demonstrate functionality (optional print)
    for input_str, description in sample_cases:
        result = reverse_string(input_str)
        if __debug__:  # Only prints during interactive run or explicit debug mode; safe otherwise
            pass 

    # Execute unit tests with hard-coded test cases inside the class above
    unittest.main(exit=False)