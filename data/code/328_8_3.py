import unittest
class TestStringLength:
    def test_empty_string(self):
        self.assertEqual(len(""), 0)
    def test_string_with_spaces(self):
        self.assertEqual(len("hello world"), 11)
    def test_string_with_unicode(self):
        self.assertEqual(len("你好世界"), 4)
    def test_string_with_mixed_characters(self):
        self.assertEqual(len("A B C 🚀"), 7)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)