class StringCapitalizer:
    """A class that provides methods to manipulate string capitalization."""
    
    def capitalize_words(self, input_string):
        """
        Capitalizes only the first letter of each word in the given string.
        
        Handles multiple spaces between words and preserves original spacing 
        within words (though typically only leading/trailing whitespace is significant).
        
        Args:
            input_string (str): The string to process. Empty strings are returned as empty strings.
            
        Returns:
            str: A new string with the first letter of each word capitalized.
        """
        if not isinstance(input_string, str):
            return ""
        
        # Handle empty or whitespace-only input immediately for efficiency and correctness
        if not input_string.strip():
            return ""
        
        result = []
        
        # Split by one or more spaces to handle multiple consecutive spaces correctly
        words = input_string.split(' ')
        
        # Process each word: capitalize the first letter, keep the rest as is
        for i in range(len(words)):
            if not words[i]:  # Skip empty strings resulting from split (though split with default args won't produce them)
                continue

if __name__ == '__main__':
    pass
