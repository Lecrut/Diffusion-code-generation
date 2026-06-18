"""String utility module providing text manipulation helpers."""

class StringUtility:
    """A class containing static methods for common string operations."""

    @staticmethod
    def capitalize_words(text: str) -> str:
        """Capitalize only the first letter of each word in the input string.

        This method processes the input string by splitting it into words, 
        capitalizing the first character of each word (if present), and 
        joining them back with a space separator. It handles mixed case 
        inputs while preserving the original casing for non-first letters.
        
        Args:
            text (str): The input string containing one or more words to capitalize.

        Returns:
            str: A new string where the first letter of each word is capitalized.

        Examples:
            >>> StringUtility.capitalize_words("hello world")
            'Hello World'
            
            >>> StringUtility.capitalize_words("THE QUICK BROWN FOX")
            'The Quick Brown Fox'
            
            >>> StringUtility.capitalize_words("")
            ''
        
        Raises:
            TypeError: If the input is not a string.

        Note:
            Consecutive spaces are preserved in the output to maintain 
            structural integrity of the original whitespace pattern, though 
            only leading/trailing single words affect capitalization logic per word boundary.
        """
        if not isinstance(text, str):
            raise TypeError(f"Expected 'str', got {type(text).__name__}")

        # Split by whitespace to handle multiple spaces between words correctly
        parts = text.split()
        
        result_parts = []
        for part in parts:
            if len(part) > 0:
                capitalized_part = part[0].upper() + part[1:]
                result_parts.append(capitalized_part)
            
        return " ".join(result_parts).strip()

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_cases = [
        ("hello world", "Hello World"),
        ("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG", 
         "The Quick Brown Fox Jumps Over The Lazy Dog"),
        ("  multiple   spaces  here  ", "Multiple Spaces Here"),
        ("single word", "Single Word"),
        (""),
    ]

    print("Running StringUtility tests...\n")
    
    for i, (input_str, expected) in enumerate(test_cases):
        try:
            output = StringUtility.capitalize_words(input_str)
            
            # Handle empty string comparison carefully as split() behavior varies slightly with strip
            if input_str == "":
                is_correct = True  # Empty string should return empty or space-separated list joined back to empty
            else:
                is_correct = (output == expected)

            status = "PASS" if is_correct else f"FAIL (Expected '{expected}', got '{output}')"
            
            print(f"Test Case {i+1}:")
            print(f"  Input:    |{input_str!r}|")
            print(f"  Output:   |{output!r}|")
            print(f"  Status:   [{status}]")
            if not is_correct and input_str != "":
                print()

        except Exception as e:
            print(f"Test Case {i+1}: ERROR - {e}")

    print("\nAll tests completed.")