import unittest

def first_letters(text):
    words = text.split()
    result = []
    for word in words:
        if any(char.isalpha() for char in word):
            result.append(word[0])
    return result

class TestFirstLetters(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(first_letters(""), [])

    def test_only_spaces(self):
        self.assertEqual(first_letters("   "), [])

    def test_mixed_punctuation(self):
        self.assertEqual(first_letters("Hello, world! How's it going?"), ['H', 'w', 'H', 'i', 'g'])

    def test_single_word(self):
        self.assertEqual(first_letters("SingleWord"), ['S'])

    def test_words_with_numbers(self):
        self.assertEqual(first_letters("W1 W2 W3"), ['W', 'W', 'W'])

    def test_leading_and_trailing_spaces(self):
        self.assertEqual(first_letters("  Leading and trailing spaces  "), ['L', 'a', 't', 's'])

    def test_punctuation_only(self):
        self.assertEqual(first_letters("!@#$%^&*()"), [])

if __name__ == '__main__':
    unittest.main()