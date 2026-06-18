class StringCaseManipulator:
    """A class to efficiently manipulate string cases."""

    @staticmethod
    def convert_to_lower(s: str) -> str:
        """Convert a string to all lowercase letters."""
        return s.lower()

    @staticmethod
    def convert_to_upper(s: str) -> str:
        """Convert a string to all uppercase letters."""
        return s.upper()

    @staticmethod
    def convert_to_title(s: str) -> str:
        """Convert the first character of each word to uppercase and the rest to lowercase."""
        # Using title() is efficient in CPython, but we ensure it handles non-alphabetic chars correctly as per standard behavior.
        return s.title()

    @staticmethod
    def get_case_format(s: str) -> dict:
        """Return a dictionary containing all three case formats for the given string."""
        return {
            "lower": StringCaseManipulator.convert_to_lower(s),
            "upper": StringCaseManipulator.convert_to_upper(s),
            "title": StringCaseManipulator.convert_to_title(s)
        }

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    test_string = "Hello, World! This is a Python script."

    print(f"Original: {test_string}")
    
    result_formats = StringCaseManipulator.get_case_format(test_string)
    
    print("\nFormatted Cases:")
    for case_name, formatted_str in result_formats.items():
        # Using f-string with explicit formatting to ensure clarity.
        print(f"{case_name.capitalize()}: {formatted_str}")

    # Demonstrate individual method calls as well.
    print("\nIndividual Method Calls:")
    lower_result = StringCaseManipulator.convert_to_lower(test_string)
    upper_result = StringCaseManipulator.convert_to_upper(test_string)
    
    print(f"Lowercase:   '{lower_result}'")
    print(f"Uppercase:   '{upper_result}'")