import unittest
def combine_words(word1: str, word2: str) -> str:
    return f"{word1.upper()} {word2.lower()}"
class TestCombineWords(unittest.TestCase):
    def test_combines_basic(self):
        self.assertEqual(combine_words("hello", "world"), "HELLO world")
    def test_empty_first_word(self):
        self.assertEqual(combine_words("", "test"), "" + "TEST".lower())
    def test_empty_second_word(self):
        result = combine_words("input", "")
        expected = "INPUT" + "".join(c.lower() for c in "") if len(result) > 0 else ""
        self.assertEqual(combine_words("test", ""), "TEST")
    def test_special_characters(self):
        result = combine_words("!@#", "$%^&*")
        expected = "!@#" + "$%^&*".lower()
        self.assertEqual(result, expected)
if __name__ == '__main__':
    unittest.main(exit=False)