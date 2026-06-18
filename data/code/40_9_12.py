import unittest

def extract_first_letters(text: str) -> list[str]:
    """Extracts the first letter of each word from a string."""
    words = text.split()
    return [word[0] if word else "" for word in words]

class TestExtractFirstLetters(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(extract_first_letters(""), [])

    def test_only_spaces(self):
        self.assertEqual(extract_first_letters("   "), [])

    def test_mixed_punctuation(self):
        # Words like "hello," or "...world" should still yield 'h' and 'w' based on split() behavior.
        result = extract_first_letters("Hello, World! ...")
        expected = ["H", "W"]  # split removes punctuation attached to words in this simple implementation logic if using default split, 
                              # but standard split keeps internal chars. Let's verify: "hello," -> word is "hello,", first char 'h'.
        self.assertEqual(result, expected)

    def test_single_word(self):
        result = extract_first_letters("Python")
        self.assertEqual(result, ["P"])

    def test_multiple_words_mixed_case(self):
        text = "Hello World PYTHON"
        result = extract_first_letters(text)
        expected = ["H", "W", "P"]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    # Hard-coded sample values for demonstration (not used in actual test execution logic above but satisfy requirement context if needed elsewhere)
    SAMPLE_CASES = [
        ("", []),
        ("   ", []),
        ("Hello World!", ["H", "W"]),
        ("a b c", ["a", "b", "c"]),
        ("Test Case 123", ["T", "C"])
    ]

    suite = unittest.TestLoader().loadTestsFromTestCase(TestExtractFirstLetters)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Optional: Run sample cases manually if desired for interactive checking without input prompts
    print("\n--- Manual Sample Verification ---")
    all_passed = True
    for text, expected in SAMPLE_CASES:
        actual = extract_first_letters(text)
        passed = actual == expected
        status = "PASS" if passed else "FAIL"
        print(f"{status}: '{text}' -> {actual} (expected {expected})")