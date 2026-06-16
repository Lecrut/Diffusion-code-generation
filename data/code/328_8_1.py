import unittest
class TestStringLength:
    def test_empty_string(self):
        self.assertEqual(len(""), 0)
    def test_string_with_spaces(self):
        self.assertEqual(len("hello world"), 11)
        self.assertEqual(len("   "), 3)
    def test_string_with_unicode(self):
        self.assertEqual(len("résumé"), 6)
        self.assertEqual(len("你好"), 2)
        self.assertEqual(len("🚀✨"), 2)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)