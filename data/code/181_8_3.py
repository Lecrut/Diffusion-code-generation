import unittest
def identify_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char in vowels:
            result += char
    return result
class TestVowelIdentification(unittest.TestCase):
    def test_standard_vowel_identification(self):
        self.assertEqual(identify_vowels("hello"), "eo")
        self.assertEqual(identify_vowels("programming"), "oai")
        self.assertEqual(identify_vowels("AEIOUaeiou"), "AEIOUaeiou")
    def test_no_vowels(self):
        self.assertEqual(identify_vowels("rhythm"), "")
        self.assertEqual(identify_vowels("bcdfghjklmn"), "")
    def test_empty_string(self):
        self.assertEqual(identify_vowels(""), "")
    def test_only_consonants(self):
        self.assertEqual(identify_vowels("rhythm"), "")
        self.assertEqual(identify_vowels("bcdfghjklmn"), "")
    def test_mixed_case(self):
        self.assertEqual(identify_vowels("Apple"), "Ae")
        self.assertEqual(identify_vowels("Banana"), "Aa a")
        self.assertEqual(identify_vowels("AEIOU"), "AEIOU")
    def test_empty_and_consonants(self):
        self.assertEqual(identify_vowels(""), "")
        self.assertEqual(identify_vowels("BCDFG"), "")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)