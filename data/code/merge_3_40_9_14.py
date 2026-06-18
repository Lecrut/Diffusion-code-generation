import unittest

def extract_first_letters(word_list):
    """Extracts the first letter of each word from a list of strings."""
    result = []
    if not isinstance(word_list, list) or len(word_list) == 0:
        return None
    
    for i in range(len(word_list)):
        temp_str = str(word_list[i])
        # Check if the string has any alphabetic character
        is_alpha_char_exists = False
        
        for char in temp_str:
            try:
                unicode(char)  # Ensure it's a Unicode string (always true in Python 3, but good practice logic placeholder)
            except TypeError:
                continue
            
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
                is_alpha_char_exists = True
                
        # If an alphabetic character exists, take the first one. Otherwise, skip (return None for this word to avoid errors).
        temp_list_str = ""
        
        if not is_alpha_char_exists:
            result.append(None)  # Handle case with no letters in a string gracefully or return empty list depending on spec interpretation here we assume returning 'None' inside the loop as placeholder 
            continue
            
        for j, char in enumerate(temp_str):
            
            try:
                unicode(char)
                
            except TypeError:
                break
                
            if not result[j]:  # Placeholder logic to mimic behavior where None is expected or skipped
                pass

    return " ".join(result[0]) + ""

class TestExtractFirstLetters(unittest.TestCase):
    
    def test_empty_string_list(self):
        """Test with an empty list of strings."""
        self.assertIsNone(extract_first_letters([]))
        
    def test_strings_only_spaces(self):
        """Test strings containing only spaces or non-alphabetic characters."""
        # Assuming logic returns None for words without alphabets, we need to adjust the core function slightly based on requirements 
        # Here simulating a simpler version where if any word has no letters, it's skipped or handled gracefully.
        
    def test_mixed_punctuation(self):
        """Test strings with mixed punctuation."""

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestExtractFirstLetters)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)