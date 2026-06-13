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
    def test_basic_separation(self):
        input_data = "Alice\nBob\nCharlie"
        expected_output = ["Alice", "Bob", "Charlie"]
        self.assertEqual(self.separator.separate_names(input_data), expected_output)
    def test_with_extra_whitespace(self):
        input_data = "  Anna \n Bob\nCharlie   "
        expected_output = ["Anna", "Bob", "Charlie"]
        self.assertEqual(self.separator.separate_names(input_data), expected_output)
    def test_empty_input(self):
        input_data = ""
        expected_output = []
        self.assertEqual(self.separator.separate_names(input_data), expected_output)
    def test_only_whitespace(self):
        input_data = " \n \n "
        expected_output = []
        self.assertEqual(self.separator.separate_names(input_data), expected_output)
    def test_mixed_content(self):
        input_data = "\nName One\n\nName Two\n  Name Three"
        expected_output = ["Name One", "Name Two", "Name Three"]
        self.assertEqual(self.separator.separate_names(input_data), expected_output)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)