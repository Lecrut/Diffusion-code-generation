import unittest
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count
class TestVowelCounter(unittest.TestCase):
    def test_standard_case(self):
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("world"), 1)
        self.assertEqual(count_vowels("programming"), 4)
    def test_empty_string(self):
        self.assertEqual(count_vowels(""), 0)
    def test_only_consonants(self):
        self.assertEqual(count_vowels("rhythm"), 0)
        self.assertEqual(count_vowels("bcdfghjklmn"), 0)
    def test_only_vowels(self):
        self.assertEqual(count_vowels("aeiou"), 5)
        self.assertEqual(count_vowels("AEIOU"), 5)
    def test_mixed_case(self):
        self.assertEqual(count_vowels("Apple"), 2)
        self.assertEqual(count_vowels("Elephant"), 3)
        self.assertEqual(count_vowels("aEiOu"), 5)
    def test_complex_string(self):
        self.assertEqual(count_vowels("Testing Vowel Counting"), 6)
        self.assertEqual(count_vowels("Rhythm and the sky"), 4)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)