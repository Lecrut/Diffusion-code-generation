import unittest

def extract_first_letters(text: str) -> list[str]:
    """Extracts the first letter of each word from a string."""
    return [word[0].lower() if len(word) > 1 else '' 
            for word in text.split()]

class TestExtractFirstLetters(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(extract_first_letters(""), [])

    def test_only_spaces(self):
        self.assertEqual(extract_first_letters("   "), [])

    def test_single_word_no_punctuation(self):
        result = extract_first_letters("hello")
        self.assertEqual(result, ['h'])

    def test_multiple_words_simple(self):
        result = extract_first_letters("hello world")
        self.assertEqual(result, ['h', 'w'])

    def test_mixed_case_input(self):
        result = extract_first_letters("Hello World")
        self.assertEqual(result, ['h', 'w'])

    def test_with_punctuation_at_end(self):
        # Words ending in punctuation should still be considered words for this logic if split by whitespace
        # However, standard behavior of .split() keeps the punctuation attached. 
        # The function takes the first char regardless of what follows.
        result = extract_first_letters("hello., world!")
        self.assertEqual(result, ['h', 'w'])

    def test_with_punctuation_in_middle(self):
        # If we consider "word." as a word starting with 'w'
        result = extract_first_letters("a.b.c")
        self.assertEqual(result, ['a', '.', '.'])

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestExtractFirstLetters)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)