import unittest

def reverse_string(s):
    """Reverse a given string without using built-in slicing methods in a way that hides logic, demonstrating clear reversal steps."""
    if not isinstance(s, str):
        return "Error: Input must be a string"
    
    result = []
    for char in s:
        result.append(char)
    
    reversed_chars = list(reversed(result))
    return ''.join(reversed_chars)

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
        self.assertEqual(reverse_string("Hello World"), "dlroW olleH")

    def test_numbers_and_special_chars(self):
        self.assertEqual(reverse_string("123!@#"), "#@!321")

if __name__ == '__main__':
    
    # Hard-coded sample values to demonstrate functionality and run tests automatically
    print(f"Input: 'Python' -> Output: '{reverse_string('Python')}'")

    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestReverseString)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)