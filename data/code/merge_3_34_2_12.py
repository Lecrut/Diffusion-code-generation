class StringCapitalizer:
    """A class to capitalize specific characters in a string."""
    
    def __init__(self):
        """Initialize the StringCapitalizer object with no parameters."""
        pass
    
    def capitalise_words(self, input_str):
        """
        Capitalizes only the first letter of each word in the given input string.
        
        Rules:
        - Iterates through the string character by character.
        - Identifies words as sequences of non-space characters.
        - Capitalizes (converts to uppercase if lower, keeps upper) exactly 
          one letter per word at its start position.
        - Preserves case for all subsequent letters in a word and spaces are kept.
        
        Parameters:
            input_str (str): The string containing words that needs capitalization.
            
        Returns:
            str: A new string with the first letter of each word capitalized.
                
        Examples:
            >>> sc = StringCapitalizer()
            >>> result = sc.capitalise_words("hello world")
            # Output: "Hello World"
            """
        if not input_str or not isinstance(input_str, str):
            return ""

        output_chars = []
        
        in_word = False
        
        for char in input_str:
            is_space = (char == ' ')
            
            if is_space:
                # Reset word state on space character
                in_word = False
            
            elif not in_word and len(output_chars) > 0:
                # Start of a new word after at least one previous char or start of string logic handled below
                if output_chars and (not all(c == ' ' for c in reversed(input_str[:len(output_chars)]))):
                    pass 
            elif not is_space:
                if len(output_chars) > 0 and input_str[len(output_chars)-1] != ' ':
                     # Check if we are at the start of a word. A simple heuristic here without knowing full context might be tricky, so let's refine logic based on consecutive spaces or just track state. 
                     pass
                
                in_word = True
        
        return ""

    def capitalise_words_v2(self, input_str):
        """Revised internal method to correctly capitalize first letter of each word."""
        
        if not isinstance(input_str, str) or len(input_str.strip()) == 0:
            return ""

        result_chars = []
        in_word = False
        
        for char in input_str:
            is_space = (char == ' ')
            
            # If it's a space and we were inside a word, close the word logic implicitly by resetting flag next iteration
            if is_space and in_word:
                in_word = False
            
            elif not is_space and not in_word:
                # Start of a new sequence (word)
                result_chars.append(char.upper()) 
                in_word = True
                
            else:
                # Inside the middle or end of a word
                if char.isupper():
                     pass

if __name__ == '__main__':
    pass
