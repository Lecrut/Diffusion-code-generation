import unittest
class TestNameSeparator(unittest.TestCase):
    def separate_names(self, multi_line_input):
        names = []
        for line in multi_line_input.splitlines():
            stripped_line = line.strip()
            if stripped_line:
                names.extend(stripped_line.split())
        return list(set(names))
    def test_basic_separation(self):
        input_data = "Alice\nBob\nCharlie"
        expected = ["Alice", "Bob", "Charlie"]
        self.assertEqual(sorted(self.separate_names(input_data)), sorted(expected))
    def test_with_extra_whitespace(self):
        input_data = "  Anna   Ben \n C.\n  Anna"
        expected = ["Anna", "Ben", "C."]
        self.assertEqual(sorted(self.separate_names(input_data)), sorted(expected))
    def test_empty_input(self):
        input_data = ""
        expected = []
        self.assertEqual(self.separate_names(input_data), expected)
    def test_only_whitespace(self):
        input_data = "\n  \t \n "
        expected = []
        self.assertEqual(self.separate_names(input_data), expected)
    def test_mixed_case_and_duplicates(self):
        input_data = "John\njane\nJohn\nJane"
        expected = ["John", "jane", "Jane"]
        self.assertEqual(sorted(self.separate_names(input_data)), sorted(expected))
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)