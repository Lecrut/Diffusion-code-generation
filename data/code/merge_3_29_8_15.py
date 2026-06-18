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
        result = reverse_string("radar")
        self.assertTrue(result == result[::-1])  # Reverse of palindrome is itself, but we just verify the function output matches expected reversed form.
        
    def test_mixed_case_and_spaces(self):
        input_str = "Hello World!"
        expected_output = "!dlroW olleH"
        self.assertEqual(reverse_string(input_str), expected_output)

    def test_numeric_characters(self):
        result = reverse_string("12345")
        self.assertEqual(result, "54321")

if __name__ == '__main__':
    # Hard-coded sample execution to demonstrate functionality without user input
    print(f"Original: 'Python' -> Reversed: {reverse_string('Python')}")
    
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringReversal)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)