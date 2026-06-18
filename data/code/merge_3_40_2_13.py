class FirstLetterExtractor:
    """A class to extract the first letter of each word from a given text."""
    
    def extract(self, text):
        """
        Returns the first letter of every word in the input text as a string.
        
        Args:
            text (str): The input text containing words separated by whitespace or punctuation.
            
        Returns:
            str: A concatenated string of the first letters of each alphabetic character 
                 found at the start of any sequence of non-space, non-punctuation characters.
        """
        import re
        
        # Compile regex for efficiency (though in single-line usage it's negligible)
        pattern = re.compile(r'\b[a-zA-Z]')
        
        # Find all matches which represent words starting with a letter
        first_letters = list(pattern.finditer(text))
        
        # Extract the character and join them, handling case sensitivity as per original logic usually implied (lowercase or mixed)
        # The requirement says "first letter", implying preserving case unless specified otherwise. 
        # However, often these tasks imply lowercasing for normalization. Let's stick to raw extraction first char of match groups.
        
        result = ''.join(match.group(0)[0] for match in pattern.finditer(text))
        
        return result

if __name__ == '__main__':
    extractor = FirstLetterExtractor()
    
    # Hard-coded sample values without user input, arguments, or files
    samples = [
        "Hello World",
        "Python Programming is Fun!",
        "...start here...",
        """Multiple   spaces and punctuation?""",
    ]

    for text in samples:
        output = extractor.extract(text)
        print(f"Input: '{text}'")
        print(f"Output: {output}\n")