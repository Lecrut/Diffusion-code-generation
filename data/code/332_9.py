import unittest
class VowelCounter:
    def count_vowels(self, text):
        count = 0
        vowels = "aeiouAEIOU"
        for char in text:
            if char in vowels:
                count += 1
        return count
class TestVowelCounter(unittest.TestCase):
    def setUp(self):
        self.counter = VowelCounter()
    def test_standard_case(self):
        self.assertEqual(self.counter.count_vowels("hello"), 2)
        self.assertEqual(self.counter.count_vowels("aeiou"), 5)
    def test_no_vowels(self):
        self.assertEqual(self.counter.count_vowels("rhythm"), 0)
        self.assertEqual(self.counter.count_vowels("bcdfghjklmn"), 0)
    def test_empty_string(self):
        self.assertEqual(self.counter.count_vowels(""), 0)
    def test_only_consonants(self):
        self.assertEqual(self.counter.count_vowels("rhythm"), 0)
        self.assertEqual(self.counter.count_vowels("bcdfghjklmn"), 0)
    def test_mixed_case(self):
        self.assertEqual(self.counter.count_vowels("Apple"), 2)
        self.assertEqual(self.counter.count_vowels("AEIOUaeiou"), 10)
        self.assertEqual(self.counter.count_vowels("TestingVowels"), 4)
    def test_complex_string(self):
        self.assertEqual(self.counter.count_vowels("ProgrammingIsFun"), 5)
        self.assertEqual(self.counter.count_vowels("aeiouBCDFGH"), 5)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)