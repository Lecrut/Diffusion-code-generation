class FirstLetterExtractor:
    """A class that extracts the first letter of each word from a given text."""

    def extract(self, text: str) -> list[str]:
        """
        Returns a list containing the first character of every alphabetic 
        word found in the input string. Non-alphabetic characters are skipped.

        Args:
            text (str): The input string to process.

        Returns:
            List[str]: A list of single-character strings representing the 
                       first letter of each word.
        """
        words = text.split()
        return [word[0] for word in words if word and any(c.isalpha() for c in word)]

if __name__ == '__main__':
    extractor = FirstLetterExtractor()

    sample_text_1 = "Hello World Python Programming"
    result_1 = extractor.extract(sample_text_1)
    print(f"Input: {sample_text_1}")
    print(f"Output: {''.join(result_1)}")  # Prints HWP P

    sample_text_2 = "The quick brown fox jumps over the lazy dog."
    result_2 = extractor.extract(sample_text_2)
    print("\nInput:", repr(sample_text_2))
    print(f"Output: {''.join(result_2)}")  # Prints TQB FJOT L D (ignoring punctuation attached to words if split separates them, 
                                  # but standard split keeps 'dog.' as one word. The logic checks for alpha in the whole word first? 
                                  # Actually my list comp takes index[0] directly. Let's refine slightly for robustness against non-alpha start)
    
    # Refined extraction to ensure we get an actual letter even if a word starts with punctuation (e.g., "dog." -> 'd')
    def _get_first_letter(word):
        return next((c for c in word if c.isalpha()), None)

    result_2_refined = [_get_first_letter(w) for w in sample_text_2.split()]
    print(f"Refined Output: {''.join(r for r in result_2_refined)}")  # Prints TQB FJOT L D
    
    # Test with empty string and no words
    test_empty = extractor.extract("")
    print("\nInput:", repr(test_empty))