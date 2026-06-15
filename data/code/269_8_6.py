import unittest
def isolate_punctuation(text):
    punctuation = ""
    for char in text:
        if char in '.,!?;:"\'()[]{}':
            punctuation += char
    return punctuation
class TestIsolatePunctuation(unittest.TestCase):
    def test_standard_string(self):
        self.assertEqual(isolate_punctuation("Hello, world!"), ",!")
    def test_no_punctuation(self):
        self.assertEqual(isolate_punctuation("No punctuation here"), "")
    def test_only_punctuation(self):
        self.assertEqual(isolate_punctuation("!?."), "!?.")
    def test_empty_string(self):
        self.assertEqual(isolate_punctuation(""), "")
    def test_mixed_and_complex(self):
        self.assertEqual(isolate_punctuation("Test, this is a sentence. (with symbols)"), ",.()")
    def test_only_spaces_and_letters(self):
        self.assertEqual(isolate_punctuation("This is a test"), "")
    def test_string_with_only_punctuation_and_spaces(self):
        self.assertEqual(isolate_punctuation("! . ? "),".?! ")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)