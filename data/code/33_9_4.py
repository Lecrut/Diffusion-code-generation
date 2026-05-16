import unittest
def remove_spaces(text):
    return text.replace(' ', '')
class TestRemoveSpaces(unittest.TestCase):
    def test_no_spaces(self):
        self.assertEqual(remove_spaces("HelloWorld"), "HelloWorld")
    def test_with_multiple_spaces(self):
        self.assertEqual(remove_spaces("Hello World"), "HelloWorld")
        self.assertEqual(remove_spaces("  Extra   Spaces  "), "ExtraSpaces")
    def test_empty_string(self):
        self.assertEqual(remove_spaces(""), "")
    def test_string_with_only_spaces(self):
        self.assertEqual(remove_spaces("   "), "")
        self.assertEqual(remove_spaces("     "), "")
    def test_string_with_all_spaces(self):
        self.assertEqual(remove_spaces("     "), "")
    def test_mixed_characters(self):
        self.assertEqual(remove_spaces("a b c d"), "abcd")
        self.assertEqual(remove_spaces("Test 123"), "Test123")
        self.assertEqual(remove_spaces("  a b c  d "), "abcd")
    def test_string_with_leading_and_trailing_spaces(self):
        self.assertEqual(remove_spaces("  start and end  "), "startandend")
    def test_string_with_only_spaces_and_characters(self):
        self.assertEqual(remove_spaces("  a b  c "), "abc")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)