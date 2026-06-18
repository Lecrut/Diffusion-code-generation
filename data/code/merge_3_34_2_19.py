class StringCapitalizer:
    """A class to capitalize the first letter of each word in a string."""

    def capitalize_words(self, input_string):
        """
        Capitalizes only the first letter of each word in the given string.
        
        Non-alphabetic characters are treated as separators between words.
        Only alphabetic letters at the start of a 'word' (sequence separated 
        by non-letters) will be capitalized if they are currently lowercase.
        
        Args:
            input_string (str): The string to process.
            
        Returns:
            str: A new string with the first letter of each word capitalized.
        """
        # Split the string into words based on any non-alphabetic character boundary,
        # preserving those boundaries as spaces in the result logic implicitly by 
        # iterating through characters and tracking state. Alternatively, use regex
        # to identify start-of-word positions more robustly across edge cases like

if __name__ == '__main__':
    pass
