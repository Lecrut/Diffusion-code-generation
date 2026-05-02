import unittest
def remove_spaces(text):
    return text.replace(' ', '')
class TestRemoveSpaces(unittest.TestCase):
    def test_no_spaces(self):
        self.assertEqual(remove_spaces("HelloWorld"), "HelloWorld")
    def test_multiple_spaces(self):
        self.assertEqual(remove_spaces("Hello World"), "HelloWorld")
    def test_leading_and_trailing_spaces(self):
        self.assertEqual(remove_spaces("  Hello World  "), "HelloWorld")
    def test_string_with_only_spaces(self):
        self.assertEqual(remove_spaces("   "), "")
    def test_string_with_all_spaces(self):
        self.assertEqual(remove_spaces("     "), "")
    def test_empty_string(self):
        self.assertEqual(remove_spaces(""), "")
    def test_string_with_mixed_characters(self):
        self.assertEqual(remove_spaces("a b c d e"), "abcde")
    def test_string_with_special_characters(self):
        self.assertEqual(remove_spaces("a-b c!d"), "a-bc!d")
    def test_string_with_only_special_characters_and_spaces(self):
        self.assertEqual(remove_spaces("  !@# $ %^ "), "!@#$%^")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)