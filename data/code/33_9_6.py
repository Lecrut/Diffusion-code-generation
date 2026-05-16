import unittest
def remove_spaces(text):
    return text.replace(' ', '')
class TestRemoveSpaces(unittest.TestCase):
    def test_normal_string(self):
        self.assertEqual(remove_spaces("hello world"), "helloworld")
    def test_string_with_multiple_spaces(self):
        self.assertEqual(remove_spaces("  hello   world  "), "helloworld")
    def test_empty_string(self):
        self.assertEqual(remove_spaces(""), "")
    def test_string_with_only_spaces(self):
        self.assertEqual(remove_spaces("   "), "")
    def test_string_with_leading_and_trailing_spaces(self):
        self.assertEqual(remove_spaces("  test string  "), "teststring")
    def test_string_with_no_spaces(self):
        self.assertEqual(remove_spaces("nocspaces"), "nocspaces")
    def test_string_with_mixed_characters(self):
        self.assertEqual(remove_spaces("a b c d e"), "abcde")
    def test_string_with_special_characters(self):
        self.assertEqual(remove_spaces("a! b@ c#"), "a!b@c#")
    def test_string_with_only_spaces_and_characters(self):
        self.assertEqual(remove_spaces("  a b  c "), "abc")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)