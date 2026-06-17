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
    def test_standard_string(self):
        text = "Hello World123!"
        result = self.analyzer.analyze(text)
        self.assertEqual(result["length"], 14)
        self.assertEqual(result["alphabets"], 10)
        self.assertEqual(result["numbers"], 3)
        self.assertEqual(result["symbols"], 1)
    def test_empty_string(self):
        text = ""
        result = self.analyzer.analyze(text)
        self.assertEqual(result["length"], 0)
        self.assertEqual(result["alphabets"], 0)
        self.assertEqual(result["numbers"], 0)
        self.assertEqual(result["symbols"], 0)
    def test_only_numbers(self):
        text = "1234567890"
        result = self.analyzer.analyze(text)
        self.assertEqual(result["length"], 10)
        self.assertEqual(result["alphabets"], 0)
        self.assertEqual(result["numbers"], 10)
        self.assertEqual(result["symbols"], 0)
    def test_only_alphabets(self):
        text = "abcdefghijklmnopqrstuvwxyz"
        result = self.analyzer.analyze(text)
        self.assertEqual(result["length"], 26)
        self.assertEqual(result["alphabets"], 26)
        self.assertEqual(result["numbers"], 0)
        self.assertEqual(result["symbols"], 0)
    def test_mixed_string(self):
        text = "a1b2c3d4"
        result = self.analyzer.analyze(text)
        self.assertEqual(result["length"], 8)
        self.assertEqual(result["alphabets"], 4)
        self.assertEqual(result["numbers"], 4)
        self.assertEqual(result["symbols"], 0)
    def test_string_with_unicode(self):
        text = "Résumé €ñ🚀"
        result = self.analyzer.analyze(text)
        self.assertEqual(result["length"], 8)
        self.assertEqual(result["alphabets"], 4)                                                                      
        self.assertEqual(result["numbers"], 0)
        self.assertEqual(result["symbols"], 4)             
    def test_string_with_only_symbols(self):
        text = "!@#$%^&*()"
        result = self.analyzer.analyze(text)
        self.assertEqual(result["length"], 10)
        self.assertEqual(result["alphabets"], 0)
        self.assertEqual(result["numbers"], 0)
        self.assertEqual(result["symbols"], 10)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)