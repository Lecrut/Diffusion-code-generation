import sys

class CaseManipulator:
    """A class to efficiently manipulate string case formats."""

    def lower(self, text):
        """Converts a string to all lowercase characters."""
        return text.lower() if isinstance(text, str) else None

    def upper(self, text):
        """Converts a string to all uppercase characters."""
        return text.upper() if isinstance(text, str) else None

    def title_case(self, text):
        """Converts a string so that words start with an uppercase letter and the rest are lowercase.
        
        Args:
            text (str): The input string.

        Returns:
            str or None: Title-cased string if input is valid, otherwise None.
        """
        return text.title() if isinstance(text, str) else None

def run_demos():
    # Hard-coded sample values to avoid interactive prompts and ensure no external dependencies are needed
    
    test_string = "python programming is fun"

    manipulator = CaseManipulator()

    print(f"Original: '{test_string}'")
    
    lower_result = manipulator.lower(test_string)
    print(f"Lowercase: {lower_result}")
    
    upper_result = manipulator.upper(test_string)
    print(f"Uppercase: {upper_result}")
    
    title_result = manipulator.title_case(test_string)
    print(f"title-case: {title_result}")

if __name__ == '__main__':
    run_demos()