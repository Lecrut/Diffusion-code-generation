import unittest
class NameSeparator:
    def separate_names(self, multi_line_input):
        lines = multi_line_input.strip().split('\n')
        names = []
        for line in lines:
            if line.strip():
                names.append(line.strip())
        return names
class TestNameSeparator(unittest.TestCase):
    def setUp(self):
        self.separator = NameSeparator()
    def test_standard_input(self):
        input_data = "Alice\nBob\nCharlie"
        expected_output = ["Alice", "Bob", "Charlie"]
        self.assertEqual(self.separator.separate_names(input_data), expected_output)
    def test_input_with_empty_lines(self):
        input_data = "First Name\n\nSecond Name\n\n\nThird Name"
        expected_output = ["First Name", "Second Name", "Third Name"]
        self.assertEqual(self.separator.separate_names(input_data), expected_output)
    def test_input_with_leading_trailing_whitespace(self):
        input_data = "  Name A \n Name B \n"
        expected_output = ["Name A", "Name B"]
        self.assertEqual(self.separator.separate_names(input_data), expected_output)
    def test_empty_input(self):
        input_data = ""
        expected_output = []
        self.assertEqual(self.separator.separate_names(input_data), expected_output)
    def test_only_whitespace_input(self):
        input_data = " \n \t \n "
        expected_output = []
        self.assertEqual(self.separator.separate_names(input_data), expected_output)
    def test_single_line_input(self):
        input_data = "Single Name"
        expected_output = ["Single Name"]
        self.assertEqual(self.separator.separate_names(input_data), expected_output)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)