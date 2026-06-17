import unittest
def analyze_string(text):
    if not text:
        return {"length": 0, "alphabetic_count": 0, "numeric_count": 0, "unicode_count": 0}
    alphabetic_count = 0
    numeric_count = 0
    unicode_count = 0
    for char in text:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            alphabetic_count += 1
        elif '0' <= char <= '9':
            numeric_count += 1
        else:
            unicode_count += 1
    return {
        "length": len(text),
        "alphabetic_count": alphabetic_count,
        "numeric_count": numeric_count,
        "unicode_count": unicode_count
    }
class TestCharacterAnalysis(unittest.TestCase):
    def test_empty_string(self):
        input_str = ""
        expected = {"length": 0, "alphabetic_count": 0, "numeric_count": 0, "unicode_count": 0}
        self.assertEqual(analyze_string(input_str), expected)
    def test_only_numbers(self):
        input_str = "12345"
        expected = {"length": 5, "alphabetic_count": 0, "numeric_count": 5, "unicode_count": 0}
        self.assertEqual(analyze_string(input_str), expected)
    def test_only_letters(self):
        input_str = "HelloWorld"
        expected = {"length": 10, "alphabetic_count": 10, "numeric_count": 0, "unicode_count": 0}
        self.assertEqual(analyze_string(input_str), expected)
    def test_mixed_string(self):
        input_str = "Test123ABC"
        expected = {"length": 10, "alphabetic_count": 6, "numeric_count": 3, "unicode_count": 1}
        self.assertEqual(analyze_string(input_str), expected)
    def test_complex_unicode(self):
        input_str = "Hello🌍World!😊"
        expected = {"length": 16, "alphabetic_count": 10, "numeric_count": 0, "unicode_count": 6}
        self.assertEqual(analyze_string(input_str), expected)
    def test_only_unicode(self):
        input_str = "!@#$%^&*() "
        expected = {"length": 10, "alphabetic_count": 0, "numeric_count": 0, "unicode_count": 10}
        self.assertEqual(analyze_string(input_str), expected)
    def test_empty_unicode_only(self):
        input_str = ""
        expected = {"length": 0, "alphabetic_count": 0, "numeric_count": 0, "unicode_count": 0}
        self.assertEqual(analyze_string(input_str), expected)
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)