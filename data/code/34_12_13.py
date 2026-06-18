"""String utility class providing text manipulation helpers."""

class StringUtility:
    """A collection of static methods to perform common string operations."""

    @staticmethod
    def capitalize_words(text: str) -> str:
        """Capitalizes only the first letter of each word in the input string.

        This method processes the input string by splitting it into words, 
        capitalizing the first character of each non-empty word, and then 
        joining them back together with a single space separator to preserve 
        original spacing structure where possible (though normalization occurs).
        
        Words are defined as sequences of alphanumeric characters separated 
        by whitespace or punctuation. Non-alphanumeric leading characters in 
        words are stripped before capitalization but preserved at the end if any.

        Args:
            text (str): The input string containing one or more words to process.

        Returns:
            str: A new string where each word starts with an uppercase letter,
                 followed by its original lowercase content and non-alphabetic suffixes 
                 as they were originally found in the sequence of letters/symbols.

        Example:
            >>> StringUtility.capitalize_words("hello world")
            'Hello World'
            >>> StringUtility.capitalize_words("python is fun!")
            'Python Is Fun!'
        
        Raises:
            TypeError: If `text` is not a string instance.
            
        Note:
            This method does not modify the original input string but returns 
            a new capitalized version of it. It handles mixed case inputs by 
            converting to lowercase before capitalizing only the first letter.

        """
        
        if not isinstance(text, str):
            raise TypeError(f"Expected 'str', got {type(text).__name__}")
            
        return " ".join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    # Sample test cases to demonstrate functionality without external input.
    
    # Test Case 1: Basic sentence capitalization
    sample_1 = StringUtility.capitalize_words("hello world")
    print(f"Input: '{sample_1}'")

    # Test Case 2: Sentence with punctuation and mixed case
    sample_2 = StringUtility.capitalize_words("python is fun!")
    print(f"Input: '{sample_2}'")

    # Test Case 3: Multiple spaces between words (normalized to single space)
    sample_3 = StringUtility.capitalize_words("   multiple   spaces here ")
    print(f"Input: '{sample_3}'")

    # Test Case 4: Empty string edge case handling logic check
    empty_input = ""
    result_empty = StringUtility.capitalize_words(empty_input)
    assert result_empty == "", f"Expected empty string, got '{result_empty}'"
    
    print("All sample executions completed successfully.")