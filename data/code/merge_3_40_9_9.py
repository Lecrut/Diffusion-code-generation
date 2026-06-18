import unittest

def extract_first_letters(text: str) -> list[str]:
    """Extracts the first letter of each word from a string."""
    words = text.split()
    return [word[0] if len(word) > 1 else "" for word in words]

class TestExtractFirstLetters(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(extract_first_letters(""), [])

    def test_only_spaces(self):
        self.assertEqual(extract_first_letters("   "), [])

    def test_mixed_punctuation(self):
        result = extract_first_letters("Hello, world! How are you?")
        expected = ["H", "w", "H", "a"]
        self.assertEqual(result, expected)

    def test_single_word_no_space(self):
        self.assertEqual(extract_first_letters("Single"), [])

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestExtractFirstLetters)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Run the function with hard-coded sample values to demonstrate functionality
    samples = [
        ("", "Empty string"),
        ("   ", "Only spaces"),
        ("Hello, world! How are you?", "Mixed punctuation"),
        ("Python is great.", "Normal sentence")
    ]

    print("\n--- Function Demonstration ---")
    for text, description in samples:
        output = extract_first_letters(text)
        print(f"Input: '{text}' ({description}) -> Output: {output}")