import unittest
class NameSeparator:
    def separate_names(self, multi_line_text):
        lines = multi_line_text.strip().split('\n')
        names = []
        for line in lines:
            if line.strip():
                names.append(line.strip())
        return names
class TestNameSeparator(unittest.TestCase):
    def setUp(self):
        self.separator = NameSeparator()
    def test_basic_separation(self):
        input_text = "Alice\nBob\nCharlie"
        expected = ["Alice", "Bob", "Charlie"]
        self.assertEqual(self.separator.separate_names(input_text), expected)
    def test_with_empty_lines(self):
        input_text = "First Name\n\nSecond Name\n\n\nThird Name"
        expected = ["First Name", "Second Name", "Third Name"]
        self.assertEqual(self.separator.separate_names(input_text), expected)
    def test_leading_and_trailing_whitespace(self):
        input_text = "  Name A \n Name B \n"
        expected = ["Name A", "Name B"]
        self.assertEqual(self.separator.separate_names(input_text), expected)
    def test_empty_input(self):
        input_text = ""
        expected = []
        self.assertEqual(self.separator.separate_names(input_text), expected)
    def test_only_whitespace(self):
        input_text = " \n \t \n "
        expected = []
        self.assertEqual(self.separator.separate_names(input_text), expected)
    def test_single_line(self):
        input_text = "Single Name"
        expected = ["Single Name"]
        self.assertEqual(self.separator.separate_names(input_text), expected)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)