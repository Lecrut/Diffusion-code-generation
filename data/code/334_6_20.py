import unittest
def combine_words(word1: str, word2: str) -> str:
    return f"{word1} {word2}"
class TestCombineWords(unittest.TestCase):
    def test_basic_combination(self):
        result = combine_words("hello", "world")
        self.assertEqual(result, "hello world")
    def test_empty_string_input(self):
        result = combine_words("", "test")
        self.assertEqual(result, " test")
    def test_multiple_spaces_in_result(self):
        result = combine_words("foo bar", "baz qux")
        self.assertEqual(result, "foo bar baz qux")
if __name__ == '__main__':
    unittest.main()