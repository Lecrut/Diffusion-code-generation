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
        self.assertEqual(identify_vowels("hello world"), "eoworl")
    def test_all_vowels(self):
        self.assertEqual(identify_vowels("aeiouAEIOU"), "aeiouAEIOU")
    def test_all_consonants(self):
        self.assertEqual(identify_vowels("bcdfghjklmn"), "")
    def test_mixed_case(self):
        self.assertEqual(identify_vowels("Programming"), "oai")
    def test_empty_string(self):
        self.assertEqual(identify_vowels(""), "")
    def test_only_consonants_and_spaces(self):
        self.assertEqual(identify_vowels("rhythm sky"), "")
    def test_numbers_and_symbols(self):
        self.assertEqual(identify_vowels("a1b2c!d3e"), "ae")
    def test_complex_string(self):
        self.assertEqual(identify_vowels("Testing 123 vowels and consonants"), "eiouaeo")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)