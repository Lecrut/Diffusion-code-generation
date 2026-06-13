import unittest
class NameSeparator:
    def separate_names(self, multi_line_input):
        names = []
        for line in multi_line_input.strip().split('\n'):
            if line.strip():
                names.append(line.strip())
        return names
class TestNameSeparator(unittest.TestCase):
    def setUp(self):
        self.separator = NameSeparator()
    def test_standard_case(self):
        input_data = "Alice\nBob\nCharlie"
        expected_output = ["Alice", "Bob", "Charlie"]
        self.assertEqual(self.separator.separate_names(input_data), expected_output)
    def test_with_empty_lines(self):
        input_data = "Anna\n\nBen\n\nCathy"
        expected_output = ["Anna", "Ben", "Cathy"]
        self.assertEqual(self.separator.separate_names(input_data), expected_output)
    def test_with_leading_and_trailing_whitespace(self):
        input_data = "  David \nEve\n   Frank  "
        expected_output = ["David", "Eve", "Frank"]
        self.assertEqual(self.separator.separate_names(input_data), expected_output)
    def test_empty_input(self):
        input_data = ""
        expected_output = []
        self.assertEqual(self.separator.separate_names(input_data), expected_output)
    def test_only_whitespace(self):
        input_data = " \n \n "
        expected_output = []
        self.assertEqual(self.separator.separate_names(input_data), expected_output)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)