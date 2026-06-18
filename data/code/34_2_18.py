class StringCapitalizer:
    """A class to capitalize specific parts of a string."""
    
    def cap_first_in_words(self, text):
        """
        Capitalizes only the first letter of each word in the input string.
        
        Args:
            text (str): The input string containing words separated by spaces or other whitespace.
            
        Returns:
            str: A new string with the first character of each word capitalized, 
                 and all subsequent characters lowercase to ensure proper capitalization.
                 
        Example:
            >>> s = StringCapitalizer()
            >>> print(s.cap_first_in_words("hello world"))
            'Hello World'
            >>> print(s.cap_first_in_words("PYTHON IS COOL"))
            'Python Is Cool'
        """
        if not text or not isinstance(text, str):
            return ""
        
        # Split the string into words based on whitespace
        words = text.split()
        
        capitalized_words = []
        for word in words:
            if len(word) > 0:
                first_char = word[0].upper()
                rest_of_word = word[1:].lower()
                capitalized_words.append(first_char + rest_of_word)
            else:
                # Handle empty strings resulting from multiple spaces (though split handles this usually)
                capitalized_words.append("")
        
        return " ".join(capitalized_words)

if __name__ == '__main__':
    s = StringCapitalizer()
    
    # Sample test cases with hard-coded values
    sample_inputs = [
        "hello world",
        "PYTHON IS COOL",
        "  leading spaces   ",
        "single word",
        "",
        "a b c d e f g h i j k l m n o p q r s t u v w x y z"
    ]
    
    for sample in sample_inputs:
        result = s.cap_first_in_words(sample)
        print(f'Input: "{sample}"')
        print(f'Result: "{result}"\n')