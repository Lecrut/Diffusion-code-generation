import unittest
def isolate_punctuation(text):
    result = ""
    for char in text:
        if char in '.,?!;:"\'()[]{}':
            result += char
    return result
class TestIsolatePunctuation(unittest.TestCase):
    def test_standard_string(self):
        self.assertEqual(isolate_punctuation("Hello, world!"), ",!")
    def test_no_punctuation(self):
        self.assertEqual(isolate_punctuation("No punctuation here"), "")
    def test_only_punctuation(self):
        self.assertEqual(isolate_punctuation("!?."), "!?.")
    def test_empty_string(self):
        self.assertEqual(isolate_punctuation(""), "")
    def test_mixed_and_spaces(self):
        self.assertEqual(isolate_punctuation("A, B. C?"), ",.?")
    def test_only_spaces_and_punctuation(self):
        self.assertEqual(isolate_punctuation("  , . ! "),",.!")
    def test_complex_string(self):
        self.assertEqual(isolate_punctuation("This is a test sentence..."), "...")
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)