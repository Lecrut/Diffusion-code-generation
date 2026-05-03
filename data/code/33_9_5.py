import unittest
def remove_spaces(input_string):
    return input_string.replace(' ', '')
class TestRemoveSpaces(unittest.TestCase):
    def test_no_spaces(self):
        self.assertEqual(remove_spaces("HelloWorld"), "HelloWorld")
    def test_with_multiple_spaces(self):
        self.assertEqual(remove_spaces("Hello World"), "HelloWorld")
    def test_leading_and_trailing_spaces(self):
        self.assertEqual(remove_spaces("  Hello World  "), "HelloWorld")
    def test_string_with_only_spaces(self):
        self.assertEqual(remove_spaces("   "), "")
    def test_empty_string(self):
        self.assertEqual(remove_spaces(""), "")
    def test_string_with_all_spaces(self):
        self.assertEqual(remove_spaces("     "), "")
    def test_mixed_characters(self):
        self.assertEqual(remove_spaces("Test 1 2 3"), "Test123")
    def test_string_with_special_characters(self):
        self.assertEqual(remove_spaces("a b!c d?e"), "ab!cd?e")
    def test_string_with_only_symbols(self):
        self.assertEqual(remove_spaces("!@#$%^&*()"), "!@#$%^&*()")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)