import unittest

def remove_spaces(s: str) -> str:
    """Remove all spaces from a given string."""
    return s.replace(" ", "")

class TestRemoveSpaces(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_spaces(""), "")

    def test_only_spaces(self):
        self.assertEqual(remove_spaces("   "), "")

    def test_mixed_characters_with_spaces(self):
        input_str = "Hello World! This is a test."
        expected_output = "HelloWorld!Thisisatest."
        self.assertEqual(remove_spaces(input_str), expected_output)

    def test_no_spaces(self):
        self.assertEqual(remove_spaces("NoSpacesHere"), "NoSpacesHere")

    def test_single_space(self):
        self.assertEqual(remove_spaces("A B"), "AB")

    def test_multiple_consecutive_spaces(self):
        self.assertEqual(remove_spaces("A  B   C"), "ABC")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRemoveSpaces)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Run the function with hard-coded sample values to demonstrate functionality
    print("\n--- Function Demonstration ---")
    samples = [
        "",
        "   ",
        "Hello World!",
        "NoSpaces",
        "A  B   C"
    ]
    
    for sample in samples:
        output = remove_spaces(sample)
        print(f"Input: {repr(sample)} -> Output: {repr(output)}")

    # Exit with error code if any tests failed
    exit(result.wasSuccessful() and not result.errors and not result.failures or 0, 1)