import unittest

def extract_first_letters(text: str) -> list[str]:
    """Extracts the first letter of each word in a string."""
    if not text or not text.strip():
        return []
    
    # Split by whitespace to get words, filter out empty strings
    words = [word for word in text.split() if word]
    
    result = []
    for word in words:
        first_char = word[0].strip('.,!?;:"\'')  # Remove common punctuation from start of word
        if first_char.isalpha():
            result.append(first_char)
        else:
            # If the character after stripping is still not alpha, take next valid char or skip
            for ch in word:
                if ch.isalpha():
                    result.append(ch)
                    break
    
    return result

class TestExtractFirstLetters(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(extract_first_letters(""), [])

    def test_only_spaces(self):
        self.assertEqual(extract_first_letters("   "), [])

    def test_mixed_punctuation(self):
        # "Hello, World! How are you?" -> ['H', 'W', 'H']
        result = extract_first_letters("Hello, World! How are you?")
        expected = ["H", "W", "H"]
        self.assertEqual(result, expected)

    def test_special_punctuation_start(self):
        # Starts with punctuation like quotes or dashes
        result = extract_first_letters("'Sunny day' and -123 stop.")
        # Expected: ' (from Sunny), a (from and), s (from stop after removing dash if treated as separator, but here split handles spaces)
        # Let's trace carefully: 
        # " 'Sunny" -> word "'Sunny", strip start punctuation -> "Sunny" -> first char 'S'
        # Wait, my logic strips the FIRST character. If it is not alpha, I loop through to find alpha.
        # Word 1: "'Sunny". Strip? No, only stripped at index 0 check initially fails. Loop finds S. Result ['S']... wait no.
        # My code does word[0].strip() if exists else ... 
        # Let's re-verify logic for " 'Sunny day"
        # Split: ["'Sunny", "day"]
        # 1. "'Sunny". char = "'" (not alpha). Loop finds S. Append S. -> ['S']? No, wait.
        # The previous implementation was slightly flawed in the thought process above regarding 'strip'. 
        # Let's fix logic to be robust: take first alphabetic character of each word found by split().
        
        # Refined Logic for test case " 'Sunny day" -> ['S', 'd']? No, usually we want words.
        # If input is "'Sunny", it should probably return 'S'. 
        # My code: first_char = "'" (not alpha). Loop finds S. Append S. Correct.
        
        result = extract_first_letters("'Sunny day")
        expected = ["S", "d"]
        self.assertEqual(result, expected)

    def test_mixed_case(self):
        text = "Python 3 is great!"
        # 'P', 'i' (from is), 'g' (no wait, from great -> g). 
        result = extract_first_letters(text)
        expected = ["P", "i", "g"]
        self.assertEqual(result, expected)

    def test_numeric_only(self):
        text = "123 456"
        # Should return empty or skip non-alpha. My logic appends first alpha found. 
        # Since no alpha exists in numbers, it should be [].
        result = extract_first_letters(text)
        expected = []
        self.assertEqual(result, expected)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestExtractFirstLetters)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)