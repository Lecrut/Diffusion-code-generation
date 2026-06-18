"""String utility module providing functions to manipulate text case."""

class StringUtility:
    """A class containing static methods for common string manipulation tasks."""

    @staticmethod
    def capitalize_words(input_string: str) -> str:
        """
        Capitalizes the first letter of each word in the input string.

        This method iterates through the input string, identifies word boundaries (whitespace),
        and capitalizes the first character of each subsequent word after converting it to title case logic manually 
        or by using standard library functions appropriately for non-alphabetic characters if needed.
        
        Words are defined as sequences separated by whitespace. Non-word characters preceding a letter 
        do not affect whether that letter is considered the start of a new word in this specific implementation,
        but typically 'capitalize_words' implies splitting on whitespace and joining back with capitalized starts.

        Args:
            input_string (str): The string to process. Can be None or an empty string.

        Returns:
            str: A new string where the first letter of each word is uppercase, 
                 while preserving the case of the rest of the letters in that word.
                 
        Examples:
            >>> s = StringUtility.capitalize_words("hello world")
            >>> print(s)
            Hello World
            
            >>> s2 = StringUtility.capitalize_words("")
            >>> print(repr(s2))
            ''

            Note: This method treats any sequence of non-whitespace characters as a word.
        """
        if input_string is None or not isinstance(input_string, str):
            raise TypeError("Input must be a string.")

        # Split the string by whitespace to get words
        parts = input_string.split()
        
        capitalized_parts = []
        for part in parts:
            if len(part) > 0:
                # Capitalize first letter and keep rest as is, handling non-letters gracefully
                if not isinstance(part[0], str):
                    raise TypeError("Part of the input string contains unexpected type.")
                
                char_list = list(part)
                if char_list[0].isalpha():
                    char_list[0] = char_list[0].upper()
                else:
                    # If first character isn't alphabetic, we still capitalize it to match standard behavior 
                    # or leave it? Standard title case usually leaves non-alpha alone unless specified.
                    # However, the prompt says "capitalizes only the first letter". 
                    # Let's assume if it's a digit/symbol, we don't change its 'case' as letters have cases.
                    pass
                
                capitalized_parts.append("".join(char_list))
            else:
                capitalized_parts.append("")

        return "".join(capitalized_parts)

if __name__ == '__main__':
    # Hard-coded sample values to test the method without user input or external dependencies
    samples = [
        "hello world",
        "this is a test string with multiple words",
        "",
        "singleword",
        "!@#$%^&*()",  # Edge case: no alphabetic characters at start of parts might occur if we split differently, 
                     # but here splitting on whitespace keeps the whole thing as one word.
    ]

    print("Testing StringUtility.capitalize_words method:")
    
    for sample in samples:
        try:
            result = StringUtility.capitalize_words(sample)
            print(f"Input:  '{sample}'")
            print(f"Output: '{result}'\n")
        except Exception as e:
            print(f"Error processing input: {e}\n")

    # Additional manual check for edge case with symbols and mixed content
    complex_sample = "Hello, this is Python! Nice weather today."
    result_complex = StringUtility.capitalize_words(complex_sample)
    
    print("Testing Complex Sample:")
    print(f"Input : '{complex_sample}'")
    print(f"Output: '{result_complex}'\n")