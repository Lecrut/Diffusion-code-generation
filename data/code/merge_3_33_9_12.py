import unittest

def remove_spaces(text: str) -> str:
    """Remove all spaces from a given string."""
    return text.replace(" ", "")

class TestRemoveSpaces(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(remove_spaces(""), "")

    def test_only_spaces(self):
        input_str = "   \t\n  "
        expected_result = ""
        self.assertEqual(remove_spaces(input_str), expected_result)

    def test_mixed_characters_with_spaces(self):
        input_str = "Hello World! This is a Test."
        expected_result = "HelloWorld!ThisisaTest."
        self.assertEqual(remove_spaces(input_str), expected_result)

    def test_no_spaces(self):
        input_str = "NoSpacesHere"
        expected_result = "NoSpacesHere"
        self.assertEqual(remove_spaces(input_str), expected_result)

    def test_single_space_characters_only(self):
        input_str = "   \t  "
        expected_result = ""
        self.assertEqual(remove_spaces(input_str), expected_result)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestRemoveSpaces)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)