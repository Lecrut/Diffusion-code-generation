class StringCapitalizer:
    """A class providing utility to capitalize specific parts of a string."""

    def capitalize_words(self, text):
        """
        Capitalizes only the first letter of each word in the input string.
        
        Words are defined as sequences separated by whitespace or punctuation 
        that acts as a delimiter (spaces, tabs, newlines). Non-alphabetic characters 
        at the start of a 'word' segment remain unchanged if they don't form an alphabetic prefix.
        
        :param text: The input string to process.
        :type text: str
        :return: A new string with the first letter of each word capitalized.
        :rtype: str
        
        Example: 
            >>> s = StringCapitalizer()
            >>> s.capitalize_words("hello world")
            'Hello World'
            >>> s.capitalize_words("welcome to python 3.x!")
            'Welcome To Python 3.X!' (Note: logic handles alphabetic start)
        """
        if not isinstance(text, str):
            raise TypeError(f"Expected string input, got {type(text).__name__}")

        # Split the text into segments based on whitespace and punctuation that breaks word flow.
        # We use a regex to find sequences of letters/digits/underscores as words, 
        # but we need to handle cases where there might be non-alpha starts if desired logic varies.
        # Standard approach: split by whitespace first, then process each token.
        
        import re
        
        tokens = text.split()
        result_parts = []

        for token in tokens:
            # Check if the string is empty or has no alphabetic characters to capitalize at start
            clean_token = ''.join(c.lower() for c in token) 
            found_alpha = False
            
            new_chars_list = list(token)
            
            for i, char in enumerate(new_chars_list):
                if not (char.isalpha()):
                    continue
                
                # If we encounter an alphabetic character that hasn't been skipped yet, it starts a word context
                # However, the requirement is "first letter of each word". 
                # A simpler regex approach to identify words and capitalize their first char:
                
            pass

        # Refined Logic using Regex for robustness without complex manual parsing loops above
        
        import re
        
        # Pattern matches sequences that look like words (alphanumeric + underscore)
        # But we specifically want to target the start of these sequences.
        
        def capitalize_first_char(match):
            word = match.group(0).lower()
            if len(word) > 1:
                return f"{word[0].upper()}{''.join(word[1:])}"
            
            # If it's a single letter or no alpha, just return as is (or handle specific needs?) 
            # The prompt implies standard capitalization rules.
            return match.group(0)

        result = re.sub(r"\b\w", capitalize_first_char, text.lower())
        
        return result

if __name__ == '__main__':
    s = StringCapitalizer()
    
    test_cases = [
        "hello world this is a sample string",
        "welcome to python programming languages 3.x!",
        "   leading spaces here and trailing ",
        "no words at all just numbers 12345",
        "Mixed CASE Testing"
    ]

    for text in test_cases:
        output = s.capitalize_words(text)
        print(f'Input : {text!r}')
        print(f'Output:{output!r}\n')