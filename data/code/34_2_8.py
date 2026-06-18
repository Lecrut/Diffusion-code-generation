class StringCapitalizer:
    """A class to capitalize the first letter of each word in a string."""

    def capitalize_words(self, text: str) -> str:
        """
        Capitalizes only the first letter of each word in the input string.

        Args:
            text (str): The input string containing words separated by whitespace or punctuation.

        Returns:
            str: A new string with the first character of each word capitalized, 
                 preserving the original casing and spacing for subsequent characters.
        
        Example:
            >>> capitalizer = StringCapitalizer()
            >>> result = capitalizer.capitalize_words("hello world")
            >>> print(result)
            'Hello World'
            
        Note:
            Words are defined as sequences of alphabetic characters separated by non-alphabetic 
            characters or whitespace. Only the first letter of each word is affected; all other 
            letters retain their original case.

        Raises:
            TypeError: If input text is not a string.
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")

        # Split into words based on non-alphabetic characters to handle complex spacing/punctuation
        import re
        
        # Find all sequences of alphabetic characters (words) with their original surrounding context preserved via regex groups or manual processing.
        # A robust approach: iterate through the text, identify word boundaries, and capitalize only the first letter found at a new 'word' start.
        
        result_chars = []
        in_word = False
        
        for char in text.lower():  # Using lower() temporarily to detect alphabetic chars safely regardless of case logic complexity? 
            # Actually, let's stick to standard definition: A word is contiguous letters [a-zA-Z].
            pass

        # Simpler and more robust approach using regex findall with groups or manual iteration.
        # Let's use a state machine style loop for clarity without heavy imports if possible, but re is fine here.
        
        words = []
        current_word_chars = []
        
        i = 0
        while i < len(text):
            char = text[i]
            
            # Check if character is an alphabetic letter (A-Z or a-z)
            if 'a' <= char.lower() <= 'z':
                if not words:
                    current_word_chars.append(char.upper())  # Capitalize first letter of new word immediately? 
                    # Wait, we need to preserve the original case for subsequent letters in that word.
                    # So logic should be: If it's a NEW word start (previous was non-alpha or empty), capitalize this one. Else keep as is.
                    
                if not current_word_chars:
                     result_chars.append(char.upper())
                else:
                    # We are continuing the same word, but we need to check if THIS char starts a new logical block? 
                    # No, regex split is easier for "words". But we want to keep original casing inside the word.
                    
                    pass
            
            i += 1

        # Let's rewrite with clear logic:
        result = []
        
        # We will process character by character.
        # A new word starts if the current char is alphabetic and (we are at index 0 OR previous was not alphabetic).
        
        prev_was_alpha = False
        
        for i, char in enumerate(text):
            is_alpha = 'a' <= char.lower() <= 'z'
            
            # Determine if this character starts a new word
            is_new_word_start = (not prev_was_alpha and is_alpha)
            
            if is_new_word_start:
                result.append(char.upper())  # Capitalize the first letter of the word

if __name__ == '__main__':
    pass
