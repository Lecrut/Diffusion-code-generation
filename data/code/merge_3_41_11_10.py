class StringManipulator:
    """A class providing optimized string manipulation methods using built-in functions."""
    
    def to_lowercase(self, s: str) -> str:
        """Convert a given string to lowercase case.
        
        Args:
            s (str): The input string to convert.
            
        Returns:
            str: A new string with all characters converted to lowercase.
        """
        return s.lower()

    def to_uppercase(self, s: str) -> str:
        """Convert a given string to uppercase case.
        
        Args:
            s (str): The input string to convert.
            
        Returns:
            str: A new string with all characters converted to uppercase.
        """
        return s.upper()

    def to_titlecase(self, s: str) -> str:
        """Convert a given string to title case.
        
        Args:
            s (str): The input string to convert.
            
        Returns:
            str: A new string where the first character of each word is capitalized.
        """
        return s.title()

    def swapcase(self, s: str) -> str:
        """Swap the case for characters in a given string (upper becomes lower and vice versa).
        
        Args:
            s (str): The input string to process.
            
        Returns:
            str: A new string with swapped cases for each alphabetic character.
        """
        return s.swapcase()

if __name__ == '__main__':
    # Sample test values - no user interaction required
    
    sample_string = "hElLo WoRLd Python"

    manipulator = StringManipulator()

    result_lower = manipulator.to_lowercase(sample_string)
    
    result_upper = manipulator.to_uppercase(sample_string)
    
    result_title = manipulator.to_titlecase(sample_string)
    
    result_swapped = manipulator.swapcase(sample_string)

    print(f"Original:   {sample_string}")
    print(f"Lowercase:  '{result_lower}'")
    print(f"Uppercase:  '{result_upper}'")
    print(f"Title Case: '{result_title}'")
    print(f"Swap Case:  '{result_swapped}'")