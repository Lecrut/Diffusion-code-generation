class FirstLetterExtractor:
    """A class to extract the first letter of each word from a given text."""

    def __init__(self):
        pass

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
        result = []

        for word in words:
            if not word.strip():
                continue
            
            # Extract only alphabetic characters to find the first real letter
            clean_word = ''.join(char.lower() for char in word if char.isalpha())
            
            if clean_word:
                result.append(clean_word[0])

        return result

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    
    # Hard-coded sample values as per requirements (no user input, args, or network)
    samples = [
        "Hello World",
        "Python Programming is Fun!",
        "   Multiple      Spaces  Here.",
        "123 Numbers Only"
    ]

    for text in samples:
        output = extractor.extract(text)
        print(f"Input: '{text}'")
        print(f"Output: {output}")
        print("-" * 20)