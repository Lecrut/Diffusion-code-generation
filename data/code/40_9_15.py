import unittest

def extract_first_letters(text: str) -> list[str]:
    """Extracts the first letter of each word from a string."""
    words = text.split()
    return [word[0] if len(word) > 0 else '' for word in words]

class TestExtractFirstLetters(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(extract_first_letters(""), [])

    def test_only_spaces(self):
        self.assertEqual(extract_first_letters("   "), [])

    def test_mixed_punctuation(self):
        # Words like "hello," or "...world" should be split by whitespace first.
        # The function treats punctuation attached to words as part of the word unless space-separated.
        result = extract_first_letters("Hello, World! How are you?")
        self.assertEqual(result, ["H", "W", "H", "a"])

    def test_single_word(self):
        self.assertEqual(extract_first_letters("Python"), ["P"])

    def test_multiple_words_no_spaces_in_middle(self):
        # This tests the behavior when there are no spaces between words (treated as one word)
        result = extract_first_letters("HelloWorld")
        self.assertEqual(result, ["H"])

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestExtractFirstLetters)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)