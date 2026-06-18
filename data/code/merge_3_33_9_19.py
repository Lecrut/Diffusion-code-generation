import unittest

def remove_spaces(text: str) -> str:
    """Remove all spaces from the input string."""
    return text.replace(" ", "")

class TestRemoveSpaces(unittest.TestCase):
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
        self.assertEqual(remove_spaces("A B"), "AB")

    def test_multiple_consecutive_spaces(self):
        self.assertEqual(remove_spaces("A  B   C"), "ABC")

if __name__ == '__main__':
    # Run the unit tests with hard-coded sample values via setUp logic implicitly handled by TestCase methods.
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRemoveSpaces)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)