import re

class FirstLetterExtractor:
    """A class that extracts the first letter of each word from a given text."""

    def extract(self, text: str) -> list[str]:
        """
        Returns a list containing the first letter of every word in the input text.
        
        Non-alphabetic characters are treated as separators or ignored if they 
        appear at the start/end of words but no alphabetic character follows them.
        Words consist of sequences of alphanumeric and underscore characters, though
        strictly speaking for 'first letter', we look for any single alphabetical char
        that starts a word segment separated by non-alphabetic boundaries.

        Args:
            text (str): The input string to process.

        Returns:
            list[str]: A list of strings where each element is the first alphabetic 
                      character found in each 'word' component of the text.
        
        Example:
            >>> extractor = FirstLetterExtractor()
            >>> extractor.extract("Hello, World!")
            ['H', 'W']
        """
        # Split by non-alphabetic characters to isolate word segments
        words = re.split(r'[^\w]+|\b', text)

        result_chars = []

        for segment in words:
            if not segment or len(segment.strip()) == 0:
                continue
            
            first_char = None
            # Find the first alphabetic character in this segment
            for char in segment:
                if 'a' <= char.lower() <= 'z':
                    first_char = char
                    break

            if first_char is not None:
                result_chars.append(first_char)

        return result_chars

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    extractor = FirstLetterExtractor()
    
    test_cases = [
        "Hello, World!",
        "Python 3.10 is great.",
        "   Spaces and tabs here",
        "No words just punctuation !!!",
        "MixedCASE: camelCase AND PascalCase"
    ]

    for text in test_cases:
        output = extractor.extract(text)
        print(f'Input: "{text}"')
        print(f'Output: {output}')
        print("-" * 30)