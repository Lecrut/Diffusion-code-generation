import unittest

def reverse_string(s: str) -> str:
    """Reverse a given string."""
    return s[::-1]

class TestStringReversal(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_character(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_two_characters(self):
        self.assertEqual(reverse_string("ab"), "ba")

    def test_palindrome(self):
        self.assertEqual(reverse_string("radar"), "radar")

    def test_uppercase_letters(self):
        self.assertEqual(reverse_string("Hello"), "olleH")

    def test_lowercase_letters(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_mixed_case_and_spaces(self):
        self.assertEqual(reverse_string("A man a plan a canal Panama"), 
                          "amanap lanac a nalp a nam A")

    def test_numbers_and_special_chars(self):
        self.assertEqual(reverse_string("!@#$%201987-3456_"), "_#6453_-8791%$#@!")

if __name__ == '__main__':
    
    # Hard-coded sample values for demonstration (optional, to show usage)
    test_samples = [
        ("", ""),                          # Empty string
        ("hello world!", "ld!dlrow olleh"),  # Mixed content with spaces and punctuation
        ("The quick brown fox jumps over the lazy dog.", 
         ".yol zaly eht evor sedpmuj xof nworb kciuq ehT"),  # Full sentence example
    ]

    print("Running manual sample tests...")
    for i, (input_str, expected_output) in enumerate(test_samples):
        result = reverse_string(input_str)
        status = "PASS" if result == expected_output else "FAIL"
        print(f"[{status}] Test {i+1}: Input='{input_str}' | Output='{result}'")

    # Run the actual unit tests automatically
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringReversal)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    if not result.wasSuccessful():
        exit(result.failures[0][1].failureException() if result.failures else result.errors[0][1])