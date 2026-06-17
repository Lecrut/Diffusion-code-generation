import unittest
class TestVowelCounter(unittest.TestCase):
    def count_vowels(self, text):
        vowels = "aeiouAEIOU"
        count = 0
        for char in text:
            if char in vowels:
                count += 1
        return count
    def test_standard_case(self):
        self.assertEqual(self.count_vowels("hello"), 2)
        self.assertEqual(self.count_vowels("world"), 1)
        self.assertEqual(self.count_vowels("programming"), 4)
    def test_empty_string(self):
        self.assertEqual(self.count_vowels(""), 0)
    def test_only_consonants(self):
        self.assertEqual(self.count_vowels("rhythm"), 0)
        self.assertEqual(self.count_vowels("bcdfghjklmn"), 0)
    def test_only_vowels(self):
        self.assertEqual(self.count_vowels("aeiouAEIOU"), 10)
    def test_mixed_case(self):
        self.assertEqual(self.count_vowels("AEIOUaeiou"), 10)
        self.assertEqual(self.count_vowels("Apple"), 3)
        self.assertEqual(self.count_vowels("TestingVowels"), 4)
    def test_empty_and_consonants(self):
        self.assertEqual(self.count_vowels("xyz"), 0)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)