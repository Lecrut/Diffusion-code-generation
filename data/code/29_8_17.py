import unittest

def reverse_string(s: str) -> str:
    """Reverse a given string."""
    return s[::-1]

class TestReverseString(unittest.TestCase):
    
    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_character(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_normal_case(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_with_spaces(self):
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")

    def test_with_numbers(self):
        self.assertEqual(reverse_string("12345"), "54321")

    def test_special_characters(self):
        self.assertEqual(reverse_string("!@#$%"), "%$#@!")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestReverseString)
    result = unittest.TextTestRunner(verbosity=1).run(suite)

    # Run the sample cases manually to demonstrate functionality without input arguments
    samples = {
        "test case 1": reverse_string("Hello"),
        "test case 2": reverse_string(""),
        "test case 3": reverse_string("Python!"),
    }
    
    print("\n--- Sample Execution ---")
    for label, output in samples.items():
        print(f"{label}: '{output}'")

    if result.wasSuccessful():
        print("\nAll tests passed.")
    else:
        print("\nSome tests failed.")