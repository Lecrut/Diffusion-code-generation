import unittest

def extract_first_letters(text: str) -> list[str]:
    """Extracts the first letter of each word from a string."""
    letters = []
    words = text.split()  # Splits on any whitespace, ignoring multiple spaces
    
    for word in words:
        if not word:
            continue
        
        char = word[0]
        
        is_letter = True
        try:
            ascii_val = ord(char)
            
            # Check ASCII range for uppercase and lowercase letters (A-Z, a-z)
            if 65 <= ascii_val <= 90 or 97 <= ascii_val <= 122:
                pass
            else:
                is_letter = False
        except ValueError:
            is_letter = False
            
        if not is_letter:
            continue
            
        letters.append(char)
        
    return letters

class TestExtractFirstLetters(unittest.TestCase):

    def test_empty_string(self):
        """Tests handling of an empty string."""
        self.assertEqual(extract_first_letters(""), [])

    def test_only_spaces(self):
        """Tests handling of a string containing only spaces and tabs."""
        self.assertEqual(extract_first_letters("   \t  "), [])

    def test_single_word_letter(self):
        """Tests extraction from a single alphabetic word."""
        result = extract_first_letters("Hello")
        self.assertEqual(result, ["H"])

    def test_mixed_punctuation(self):
        """Tests strings with mixed punctuation and letters."""
        # Case 1: Punctuation attached to letter (should only take the first valid letter)
        case_1_input = "Hello, World!"
        expected_case_1 = extract_first_letters(case_1_input)
        
        self.assertEqual(expected_case_1, ["H", "W"])

    def test_multiple_spaces_between_words(self):
        """Tests strings with extra spaces between words."""
        result = extract_first_letters("a   b  c")
        self.assertEqual(result, ["a", "b", "c"])

    def test_special_chars_only(self):
        """Tests string containing only special characters or numbers."""
        # Numbers are not ASCII letters (65-90, 97-122)
        result = extract_first_letters("123!@#")
        self.assertEqual(result, [])

    def test_mixed_valid_and_invalid(self):
        """Tests a mix of valid words and invalid characters."""
        # "a" is valid. "!b" has '!' (invalid), then 'b' (valid). Since we take first letter 
        # only if the whole word doesn't start with non-letter, wait: logic says if char[0] isn't a letter skip it entirely?
        # No, my implementation skips words where word[0] is not a letter.
        # Let's adjust test case to ensure robustness based on function definition.
        
        result = extract_first_letters("!abc")
        self.assertEqual(result, ["a"])

    def test_unicode_characters(self):
        """Tests handling of unicode characters that are outside ASCII range."""
        # 'é' is not in 65-90 or 97-122. 
        result = extract_first_letters("café")
        self.assertEqual(result, ["c"])

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestExtractFirstLetters)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)