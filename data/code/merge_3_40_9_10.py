import unittest

def extract_first_letters(text: str) -> list[str]:
    """Extracts the first letter of each word from the input string."""
    words = text.split()
    return [word[0].lower() if len(word) > 0 else '' for word in words]

class TestExtractFirstLetters(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(extract_first_letters(""), [])

    def test_only_spaces(self):
        self.assertEqual(extract_first_letters("   "), [])

    def test_single_word_no_punctuation(self):
        result = extract_first_letters("hello")
        self.assertEqual(result, ['h'])

    def test_multiple_words_mixed_case(self):
        result = extract_first_letters("Hello World Python")
        self.assertEqual(result, ['h', 'w', 'p'])

    def test_with_punctuation(self):
        # Words like "don't" or "it's" are split by default on whitespace.
        # If the requirement implies treating punctuation attached to words as part of the word,
        # we would need a different approach (e.g., removing non-alphanumeric chars first).
        # Here we assume standard 'split()' behavior where punctuation is included in the token if no space exists.
        result = extract_first_letters("Hello, World! Python.")
        self.assertEqual(result, ['h', 'w', 'p'])

    def test_mixed_punctuation_and_spaces(self):
        text = "  Hello   , world ! python . "
        # split() handles multiple spaces and strips leading/trailing whitespace.
        result = extract_first_letters(text)
        self.assertEqual(result, ['h', 'w', 'p'])

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestExtractFirstLetters)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)