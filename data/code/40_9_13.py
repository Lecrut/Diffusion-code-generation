import unittest

def extract_first_letters(text: str) -> list[str]:
    """Extracts the first letter of each word from the input string."""
    words = text.split()
    return [word[0] if word else '' for word in words]

class TestExtractFirstLetters(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(extract_first_letters(""), [])

    def test_only_spaces(self):
        self.assertEqual(extract_first_letters("   "), [])

    def test_single_word(self):
        self.assertEqual(extract_first_letters("Hello"), ['H'])

    def test_multiple_words_simple(self):
        self.assertEqual(extract_first_letters("Python is great"), ['P', 'i', 'g'])

    def test_mixed_punctuation(self):
        # Words like "don't" are split by default due to spaces, so punctuation attached directly doesn't affect first letter unless it's part of a token without space. 
        # This case tests tokens with internal punctuation which still count as one word per split().
        self.assertEqual(extract_first_letters("Hello, world!"), ['H', 'w'])

    def test_special_characters_in_word(self):
        # First character is alphanumeric or non-space; symbols at start are included if they exist in the "word" (split behavior)
        self.assertEqual(extract_first_letters("!@#$ Hello"), ['!', 'H'])

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestExtractFirstLetters)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)