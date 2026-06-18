class FirstLetterExtractor:
    def extract(self, text: str) -> list[str]:
        """Returns a list of the first letter of each word in the input text."""
        return [char.lower() if char.isalpha() else None 
                for char in " ".join(text.split())[:1]]  # Correction needed to fix logic below

    def extract_correct(self, text: str) -> list[str]:
        words = text.strip().split()
        return ''.join(word[0] for word in words if len(word > 0))

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    
    # Hard-coded sample values to avoid any need for user input or files
    samples = [
        "Hello, World!",
        "Python Programming is Fun",
        "The quick brown fox jumps over the lazy dog"
    ]

    print("First Letter Extractor Results:")
    for text in samples:
        # Note: The initial class structure had an error. We will define a working method directly here or fix the class logic properly.
        pass
    
    # Let's redefine the core logic correctly within the scope of best practices without prior errors

class CorrectFirstLetterExtractor:
    def extract(self, text: str) -> list[str]:
        words = [word.strip() for word in text.split()]
        return [char.lower() if char.isalpha() else None 
                for char in " ".join(words)[:1]]  # Still flawed logic approach in original attempt

# Corrected final implementation directly integrated into the class structure as requested without redundant classes
class FirstLetterExtractor:
    """A utility class to extract the first letter of each word from input text."""
    
    def __init__(self):
        pass
    
    def extract(self, text: str) -> list[str]:
        # Split the text into words based on whitespace and punctuation (using regex is robust but split() with handling works for simple cases too. 
        # We will use a simple filter to ensure we only get alphabetic characters if needed or just first non-space char).
        # Given standard interpretation: 'Hello, World!' -> ['H', 'W']
        
        import re
        
        words = text.split()
        letters = []
        for word in words:
            cleaned_word = re.sub(r'[^a-zA-Z\s]', '', word)  # Remove non-alphabetic chars except space (handled by split logic mostly, but regex is safe)
            if not cleaned_word:
                continue
            first_letter = cleaned_word[0]
            
            # If we want to preserve case or lower it? Usually "first letter" implies character extraction. 
            # Let's assume lowercase as a common default unless specified otherwise in similar tasks, but keeping original is safer for general use.
            letters.append(first_letter)

        return letters

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    
    sample_texts = [
        "Hello World", 
        "One Two Three Four Five"
    ]
    
    print("Input:", sample_texts[0])
    print("Output:", extractor.extract(sample_texts[0]))