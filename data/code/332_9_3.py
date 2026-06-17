import unittest
class VowelCounter:
    def count_vowels(self, text):
        vowels = "aeiouAEIOU"
        count = 0
        for char in text:
            if char in vowels:
                count += 1
        return count
class TestVowelCounter(unittest.TestCase):
    def setUp(self):
        self.counter = VowelCounter()
    def test_standard_case(self):
        self.assertEqual(self.counter.count_vowels("hello"), 2)
        self.assertEqual(self.counter.count_vowels("programming"), 4)
    def test_empty_string(self):
        self.assertEqual(self.counter.count_vowels(""), 0)
    def test_only_consonants(self):
        self.assertEqual(self.counter.count_vowels("rhythm"), 0)
        self.assertEqual(self.counter.count_vowels("bcdfghjklmn"), 0)
    def test_only_vowels(self):
        self.assertEqual(self.counter.count_vowels("aeiouAEIOU"), 10)
    def test_mixed_case(self):
        self.assertEqual(self.counter.count_vowels("AEIOUaeiou"), 10)
        self.assertEqual(self.counter.count_vowels("TestingVowels"), 4)
    def test_with_spaces_and_punctuation(self):
        self.assertEqual(self.counter.count_vowels("Hello World!"), 3)
        self.assertEqual(self.counter.count_vowels("a b c d e"), 5)
        self.assertEqual(self.counter.count_vowels("123!@#"), 0)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)