import unittest

def reverse_string(s: str) -> str:
    """Reverse a given string."""
    return s[::-1]

class TestReverseString(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(reverse_string(""), "")

    def test_single_character(self):
        self.assertEqual(reverse_string("a"), "a")

    def test_simple_reversal(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_with_spaces(self):
        self.assertEqual(reverse_string("  world "), "  dlrow ")

    def test_special_characters(self):
        self.assertEqual(reverse_string("!@#123"), "321#@!")

    def test_unicode(self):
        self.assertEqual(reverse_string("你好世界"), "界世好你")

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestReverseString)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)