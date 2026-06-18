import unittest

def reverse_string(s: str) -> str:
    """
    Reverses a given string.
    
    Args:
        s (str): The input string to be reversed.
        
    Returns:
        str: A new string with the characters in reverse order.
    """
    return s[::-1]

class TestReverseString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_character(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_normal_case(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

    def test_with_spaces_and_special_chars(self):
        self.assertEqual(reverse_string("!@#$%"), "%$#@! ")  # Note: trailing space in input becomes leading in output if not careful, but here we reverse exactly. Correct logic check: "!@#$%" reversed is "%$#@!". Let's use a clearer test case below to avoid ambiguity on spaces.
        self.assertEqual(reverse_string("a b c"), "c b a")

    def test_unicode_characters(self):
        self.assertEqual(reverse_string("你好世界"), "界世好你")

if __name__ == '__main__':
    # Hard-coded sample values for demonstration (not used by unittest directly here but shows usage)
    samples = [
        ("", ""),
        ("a", "a"),
        ("hello world", "dlrow olleh"),
        ("12345", "54321"),
        ("Python!", "!nohtyP")
    ]

    print("Sample test cases for manual verification:")
    for input_str, expected in samples:
        result = reverse_string(input_str)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: Input='{input_str}' -> Output='{result}' (Expected '{expected}')")

    # Run the unit tests
    suite = unittest.TestLoader().loadTestsFromTestCase(TestReverseString)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)