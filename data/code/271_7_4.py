import unittest
class CharacterAnalyzer:
    def analyze(self, text):
        if not text:
            return {"length": 0, "alphabets": 0, "numbers": 0, "symbols": 0}
        alphabets = 0
        numbers = 0
        symbols = 0
        for char in text:
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
                alphabets += 1
            elif '0' <= char <= '9':
                numbers += 1
            else:
                symbols += 1
        return {"length": len(text), "alphabets": alphabets, "numbers": numbers, "symbols": symbols}
class TestCharacterAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = CharacterAnalyzer()
    def test_empty_string(self):
        text = ""
        result = self.analyzer.analyze(text)
        self.assertEqual(result["length"], 0)
        self.assertEqual(result["alphabets"], 0)
        self.assertEqual(result["numbers"], 0)
        self.assertEqual(result["symbols"], 0)
    def test_only_numbers(self):
        text = "12345"
        result = self.analyzer.analyze(text)
        self.assertEqual(result["length"], 5)
        self.assertEqual(result["alphabets"], 0)
        self.assertEqual(result["numbers"], 5)
        self.assertEqual(result["symbols"], 0)
    def test_only_alphabets(self):
        text = "HelloWorld"
        result = self.analyzer.analyze(text)
        self.assertEqual(result["length"], 10)
        self.assertEqual(result["alphabets"], 10)
        self.assertEqual(result["numbers"], 0)
        self.assertEqual(result["symbols"], 0)
    def test_mixed_string(self):
        text = "a1b2c3"
        result = self.analyzer.analyze(text)
        self.assertEqual(result["length"], 6)
        self.assertEqual(result["alphabets"], 3)
        self.assertEqual(result["numbers"], 3)
        self.assertEqual(result["symbols"], 0)
    def test_string_with_symbols(self):
        text = "a!b@c#d"
        result = self.analyzer.analyze(text)
        self.assertEqual(result["length"], 7)
        self.assertEqual(result["alphabets"], 4)
        self.assertEqual(result["numbers"], 0)
        self.assertEqual(result["symbols"], 3)
    def test_string_with_unicode(self):
        text = "Hello😊World🚀"
        result = self.analyzer.analyze(text)
        self.assertEqual(result["length"], 14)
        self.assertEqual(result["alphabets"], 5)                                                                             
        self.assertEqual(result["numbers"], 0)
        self.assertEqual(result["symbols"], 9)                                                                                       
    def test_complex_unicode_only(self):
        text = "😀🚀✨"
        result = self.analyzer.analyze(text)
        self.assertEqual(result["length"], 3)
        self.assertEqual(result["alphabets"], 0)
        self.assertEqual(result["numbers"], 0)
        self.assertEqual(result["symbols"], 3)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)