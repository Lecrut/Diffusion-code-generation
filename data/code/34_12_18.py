"""String utility module providing methods to manipulate text formatting."""

class StringUtility:
    """A class containing static string manipulation utilities."""

    @staticmethod
    def capitalize_words(text: str) -> str:
        """
        Capitalizes the first letter of each word in the input string.

        This method processes the input string by splitting it into words, capitalizing
        the first character of each non-empty word, and then joining them back together.
        It preserves the original casing for all characters except the leading ones 
        of each word segment separated by whitespace or other standard delimiters used 
        in Python's default split behavior (spaces, tabs).

        Args:
            text (str): The input string to process. Can contain any valid Unicode characters.

        Returns:
            str: A new string with the first letter of every word capitalized.
                 Words are defined as sequences separated by whitespace.

        Examples:
            >>> StringUtility.capitalize_words("hello world")
            'Hello World'
            
            >>> StringUtility.capitalize_words("  multiple   spaces ")
            ' Multiple Spaces '
            
            >>> StringUtility.capitalize_words("")
            ''
            
            >>> StringUtility.capitalize_words("no change here!")
            'No Change Here!'

        Raises:
            TypeError: If the input is not a string.
        """
        if not isinstance(text, str):
            raise TypeError(f"Expected str instance, got {type(text).__name__}")

        return " ".join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    # Sample test cases to demonstrate functionality without user input
    
    sample_inputs = [
        ("hello world", "Hello World"),
        ("  multiple   spaces ", " Multiple Spaces "),
        ("no change here!", "No Change Here!"),
        ("", ""),
        ("python programming is fun", "Python Programming Is Fun"),
        ("a b c d e f g h i j k l m n o p q r s t u v w x y z", 
         "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")
    ]

    print("Running StringUtility tests...\n")
    
    for input_str, expected_output in sample_inputs:
        result = StringUtility.capitalize_words(input_str)
        
        # Verify the output matches expectations
        if result == expected_output:
            status = "PASS"
        else:
            status = f"FAIL (Expected: '{expected_output}', Got: '{result}')"

        print(f"Input:    | {repr(input_str)}")
        print(f"Output:   | {repr(result)}")
        print(f"Status:   | [{status}]")
        print("-" * 50)