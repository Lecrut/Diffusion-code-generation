import unicodedata

class StringCaseManipulator:
    """
    A class to efficiently manipulate string case formats (lower, upper, title).
    
    Attributes:
        original_string (str): The input string to be manipulated.
        
    Methods:
        convert_to_lower() -> str: Converts the entire string to lowercase.
        convert_to_upper() -> str: Converts the entire string to uppercase.
        convert_to_title() -> str: Capitalizes each word in the string.
    
    Note: This implementation handles Unicode characters correctly for common scripts, 
            though complex combining marks might still appear as single codepoints or 
            require further normalization depending on specific use cases.
    """

    def __init__(self, original_string):
        self.original_string = original_string.strip() if isinstance(original_string, str) else ""

    def convert_to_lower(self) -> str:
        return self.original_string.lower()

    def convert_to_upper(self) -> str:
        return self.original_string.upper()

    def convert_to_title(self) -> str:
        # Python's built-in title method handles common languages well. 
        # It capitalizes the first character of each word and lowercases the rest.
        return self.original_string.title()

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input or external dependencies are needed.
    
    test_strings = [
        "hello world",
        "PYTHON IS GREAT!",
        "mixed CASE 123 with symbols! @#$"
    ]

    print("Testing StringCaseManipulator")
    print("-" * 40)

    for s in test_strings:
        manipulator = StringCaseManipulator(s)
        
        lower_result = manipulator.convert_to_lower()
        upper_result = manipulator.convert_to_upper()
        title_result = manipulator.convert_to_title()
        
        print(f"\nInput: '{s}'")
        print(f"Lowercase:   {lower_result}")
        print(f"Uppercase:   {upper_result}")
        print(f"Title Case:  {title_result}")

    # Optional simple test for Unicode handling (e.g., accented characters)
    unicode_test = "naïve café naïve"
    manipulator_unicode = StringCaseManipulator(unicode_test)
    
    lower_uni = manipulator_unicode.convert_to_lower()
    upper_uni = manipulator_unicode.convert_to_upper()
    title_uni = manipulator_unicode.convert_to_title()

    print("\nUnicode Test Input: '{0}'".format(unicode_test))
    print("Lowercase:   {0}".format(lower_uni))
    print("Uppercase:   {0}".format(upper_uni))
    print("Title Case:  {0}".format(title_uni))