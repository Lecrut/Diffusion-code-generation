import unittest
class NameSeparator:
    def separate_names(self, multi_line_input: str) -> list[str]:
        names = []
        for line in multi_line_input.strip().split('\n'):
            if line.strip():
                names.append(line.strip())
        return names
class TestNameSeparator(unittest.TestCase):
    def setUp(self):
        self.separator = NameSeparator()
    def test_basic_separation(self):
        input_data = "Alice\nBob\nCharlie"
        expected_output = ["Alice", "Bob", "Charlie"]
        self.assertEqual(self.separator.separate_names(input_data), expected_output)
    def test_with_extra_whitespace(self):
        input_data = "  Anna \n  Ben\n   Cathy  "
        expected_output = ["Anna", "Ben", "Cathy"]
        self.assertEqual(self.separator.separate_names(input_data), expected_output)
    def test_empty_input(self):
        input_data = ""
        expected_output = []
        self.assertEqual(self.separator.separate_names(input_data), expected_output)
    def test_input_with_only_whitespace(self):
        input_data = "\n  \n   "
        expected_output = []
        self.assertEqual(self.separator.separate_names(input_data), expected_output)
    def test_single_line_input(self):
        input_data = "David"
        expected_output = ["David"]
        self.assertEqual(self.separator.separate_names(input_data), expected_output)
    def test_mixed_content(self):
        input_data = "First Name\nSecond Name\n\nThird Name"
        expected_output = ["First Name", "Second Name", "Third Name"]
        self.assertEqual(self.separator.separate_names(input_data), expected_output)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)