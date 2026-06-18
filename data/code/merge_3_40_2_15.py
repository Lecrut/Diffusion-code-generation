class FirstLetterExtractor:
    """A class to extract the first letter of each word from a given text."""

    def __init__(self):
        self._cached_results = {}

    def _normalize_text(self, text: str) -> list[str]:
        """Normalize input text by converting to lowercase and splitting into words.
        
        Args:
            text (str): The raw input string containing words.
            
        Returns:
            list[str]: A list of normalized words in lower case.
        """
        # Use a regex that handles various delimiters, or simple split with maxsplit if desired logic changes later.
        # For robustness against punctuation attached to words (e.g., "hello,"), we strip non-alphabetic chars from ends before taking the first letter.
        import re
        
        # Split by whitespace and clean each word component of trailing/leading non-letters except underscores? 
        # The task implies standard English-like processing where letters are key.
        # We'll split on any character that is not a letter or digit (to handle punctuation separation).
        
        words = []
        for chunk in re.split(r'[^a-zA-Z0-9]+', text):
            if not chunk: 
                continue
                
            # Get first alphabetic char and convert to lowercase
            clean_word = ''.join(c.lower() if c.isalpha() else '' for c in chunk)
            
            # If the cleaned word is still empty (e.g., pure numbers or symbols), skip it as "letter" extraction fails.
            # However, typically we want first letter of meaningful tokens. 
            # Let's assume any alphabetic character found at start counts if possible, else return empty string? 
            # Re-reading task: "first letter of every word". A number-only token has no letter. We'll skip non-letter starts or treat as per strict definition.
            
            # To be safe and simple for general text processing: take first char that is alphabetic.
            found_char = None
            for c in chunk.lower():
                if c.isalpha():
                    found_char = c
                    break
            
            if found_char is not None:
                words.append(found_char)
                
        return words

    def extract(self, text: str) -> list[str]:
        """Extract the first letter of every word in the input text.
        
        Args:
            text (str): The string containing multiple words separated by spaces or punctuation.
            
        Returns:
            list[str]: A list where each element is a single character representing 
                       the first alphabetic letter found in the corresponding word segment, converted to lowercase.
                       
        Example:
            >>> extractor = FirstLetterExtractor()
            >>> result = extractor.extract("Hello World!")
            ['h', 'w']
            
        """
        # Normalize text and extract letters efficiently via regex split logic handled internally
        
        normalized_words = self._normalize_text(text)
        
        return normalized_words

if __name__ == '__main__':
    sample_inputs = [
        "The quick brown fox jumps over the lazy dog",
        "Python is great for data science and machine learning tasks.",
        "  Multiple   spaces    and punctuation! ? @ # $ % ^ & * ( )"
    ]

    extractor = FirstLetterExtractor()
    
    for sample in sample_inputs:
        result = extractor.extract(sample)
        print(f"\nInput text:\n{sample}\n")
        print(f"First letters extracted: {result}")