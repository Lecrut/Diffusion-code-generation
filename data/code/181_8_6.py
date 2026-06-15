import unittest
def identify_vowels(text):
    vowels = "aeiouAEIOU"
    result = ""
    for char in text:
        if char in vowels:
            result += char
    return result
class TestVowelIdentification(unittest.TestCase):
    def test_standard_case(self):
        self.assertEqual(identify_vowels("hello"), "eo")
    def test_all_vowels(self):
        self.assertEqual(identify_vowels("aeiouAEIOU"), "aeiouAEIOU")
    def test_no_vowels_consonants_only(self):
        self.assertEqual(identify_vowels("rhythm"), "")
    def test_empty_string(self):
        self.assertEqual(identify_vowels(""), "")
    def test_mixed_case(self):
        self.assertEqual(identify_vowels("Programming"), "oai")
    def test_with_spaces_and_punctuation(self):
        self.assertEqual(identify_vowels("Hello World!"), "eow o")
    def test_only_consonants(self):
        self.assertEqual(identify_vowels("bcdfghjklmn"), "")
    def test_empty_and_consonants(self):
        self.assertEqual(identify_vowels("xyz"), "")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)