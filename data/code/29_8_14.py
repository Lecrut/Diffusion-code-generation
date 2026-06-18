import unittest

def reverse_string(text: str) -> str:
    """
    Reverses a given string in place using list slicing.
    
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

    def test_simple_reversal(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_with_numbers_and_symbols(self):
        self.assertEqual(reverse_string("123!@#"), "#@!321")

    def test_unicode_characters(self):
        self.assertEqual(reverse_string("你好世界"), "界世好你")

if __name__ == '__main__':
    # Hard-coded sample values for demonstration (not part of unit tests)
    samples = [
        ("hello", "olleh"),
        ("Python 3.10", "01.3 tnohP"),
        ("", ""),
        ("a", "a"),
        ("A man, a plan, a canal: Panama!", ":amanaP :lanac ,nalp A ,nam A")
    ]

    print("Running sample tests...")
    for input_val, expected in samples:
        result = reverse_string(input_val)
        status = "PASS" if result == expected else "FAIL"
        print(f"[{status}] Input: '{input_val}' -> Expected: '{expected}', Got: '{result}'")

    # Run the actual unit tests
    suite = unittest.TestLoader().loadTestsFromTestCase(TestReverseString)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)