import unittest

def extract_first_letters(text: str) -> list[str]:
    """Extracts the first letter of each word from the input string.
    
    Args:
        text (str): The input string containing words separated by spaces or punctuation.
        
    Returns:
        list[str]: A list of single-character strings, where each character is 
                   the first alphabetic letter found in a sequence of non-space characters.
                   
    Examples:
        >>> extract_first_letters("Hello world")
        ['H', 'w']
        >>> extract_first_letters("")
        []
    """
    result = []
    
    # Split by whitespace to get potential words, but we need to handle punctuation attached to letters
    for word in text.split():
        if not word:  # Skip empty strings resulting from multiple spaces
            continue
            
        first_char = None
        
        # Iterate through characters until an alphabetic one is found or the string ends
        for char in word:
            if char.isalpha():
                result.append(char)
                break
                
    return result

class TestExtractFirstLetters(unittest.TestCase):
    
    def test_empty_string(self):
        """Test case for empty input string."""
        self.assertEqual(extract_first_letters(""), [])

    def test_only_spaces(self):
        """Test case for strings containing only spaces or newlines."""
        self.assertEqual(extract_first_letters("   \n  "), [])

    def test_simple_words(self):
        """Test basic sentence with standard words."""
        result = extract_first_letters("Hello world")
        self.assertEqual(result, ['H', 'w'])

    def test_mixed_punctuation(self):
        """Test case for strings with mixed punctuation attached to letters."""
        # Words like "hello," or "-world" should still pick the first letter
        result = extract_first_letters("Hello, world!")
        self.assertEqual(result, ['H', 'w'])

    def test_multiple_punctuation(self):
        """Test case for multiple consecutive and mixed punctuation marks."""
        text = "It's a... great day!"
        # Expected: I (from It's), a (from a), g (from great)
        result = extract_first_letters(text)
        self.assertEqual(result, ['I', 'a', 'g'])

    def test_special_characters_only(self):
        """Test case for strings containing only special characters."""
        text = "!@#$%^&*()"
        result = extract_first_letters(text)
        self.assertEqual(result, [])

    def test_mixed_case_and_punctuation(self):
        """Comprehensive test with mixed cases and various punctuation."""
        text = "Python3.8 is great! 123 ABC"
        # Expected: P (from Python), i (from is), g (from great), A (from ABC)
        result = extract_first_letters(text)
        self.assertEqual(result, ['P', 'i', 'g', 'A'])

if __name__ == '__main__':
    unittest.main()