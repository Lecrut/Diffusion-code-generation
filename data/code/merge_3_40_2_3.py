class FirstLetterExtractor:
    """A class to extract the first letter of every word from a given text."""

    def __init__(self):
        pass

    def extract(self, text: str) -> list[str]:
        """
        Returns a list containing the first letter of each word in the input text.
        
        Args:
            text (str): The input string to process.
            
        Returns:
            List[str]: A list where each element is the first character 
                       of a word found in the input text, or an empty list if no words are found.
                       
        Example:
            >>> extractor = FirstLetterExtractor()
            >>> result = extractor.extract("Hello world")
            # Returns ['H', 'w']
        """
        return [word[0] for word in text.split()]

if __name__ == '__main__':
    sample_texts = ["Python is awesome", "The quick brown fox"]
    
    extractor = FirstLetterExtractor()
    
    print("First letters extracted:")
    for original_text in sample_texts:
        result = extractor.extract(original_text)
        print(f"Input: '{original_text}' -> Output: {result}")