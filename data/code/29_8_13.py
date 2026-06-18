import unittest

def reverse_string(s: str) -> str:
    """
    Reverses a given string in-place (returns new reversed string).
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: A new string that is the reverse of the input.
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

    def test_mixed_case_and_spaces(self):
        self.assertEqual(reverse_string("Hello World!"), "!dlroW olleH")

    def test_unicode_characters(self):
        self.assertEqual(reverse_string("你好世界"), "界世好你")

if __name__ == '__main__':
    # Hard-coded sample values for demonstration (not used in unittest logic)
    samples = [
        ("hello", "olleh"),
        ("12345", "54321"),
        ("", ""),
        ("a", "a")
    ]

    print("Running manual verification on sample values:")
    for input_str, expected in samples:
        result = reverse_string(input_str)
        status = "PASS" if result == expected else "FAIL"
        print(f"Input: '{input_str}' -> Output: '{result}' (Expected: '{expected}') - {status}")

    # Run the unit tests
    unittest.main(verbosity=2)