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
        self.assertEqual(identify_vowels("programming"), "oai")
    def test_all_vowels(self):
        self.assertEqual(identify_vowels("aeiouAEIOU"), "aeiouAEIOU")
    def test_all_consonants(self):
        self.assertEqual(identify_vowels("rhythm"), "")
        self.assertEqual(identify_vowels("bcdfghjklmn"), "")
    def test_mixed_case(self):
        self.assertEqual(identify_vowels("Apple"), "Ae")
        self.assertEqual(identify_vowels("Testing"), "e")
    def test_empty_string(self):
        self.assertEqual(identify_vowels(""), "")
    def test_empty_and_consonants(self):
        self.assertEqual(identify_vowels("rhythm"), "")
        self.assertEqual(identify_vowels("bcdfghjklmn"), "")
    def test_string_with_spaces(self):
        self.assertEqual(identify_vowels("hello world"), "eo")
        self.assertEqual(identify_vowels("a b c d"), "ac")
    def test_numbers_and_symbols(self):
        self.assertEqual(identify_vowels("a1b2c!"), "ac")
        self.assertEqual(identify_vowels("aeiou123"), "aeiou")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)