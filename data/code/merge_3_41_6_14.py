class StringCaseManipulator:
    """A class to efficiently manipulate string case formats."""
    
    def __init__(self, text: str):
        """Initialize with a string."""
        self.text = text
    
    @staticmethod
    def normalize(text: str) -> str:
        """Normalize whitespace in the input string for consistent processing.
        
        Args:
            text (str): The input string to process.
            
        Returns:
            str: A normalized version of the input with single spaces and stripped ends.
        """
        return ' '.join(text.split())

    def to_lower(self) -> str:
        """Converts the current string to all lowercase letters."""
        original = self.text
        if not isinstance(original, str):
            raise TypeError("Input must be a string.")
        
        # Normalize first for consistent title case handling later
        normalized = StringCaseManipulator.normalize(original)
        return normalized.lower()

    def to_upper(self) -> str:
        """Converts the current string to all uppercase letters."""
        original = self.text
        if not isinstance(original, str):
            raise TypeError("Input must be a string.")
        
        # Normalize first for consistent title case handling later
        normalized = StringCaseManipulator.normalize(original)
        return normalized.upper()

    def to_title(self) -> str:
        """Converts the current string to Title Case (first letter of each word capitalized)."""
        original = self.text
        if not isinstance(original, str):
            raise TypeError("Input must be a string.")
        
        # Normalize first for consistent title case handling later
        normalized = StringCaseManipulator.normalize(original)
        return normalized.title()

    def get_current(self) -> str:
        """Returns the current state of the stored text."""
        if not isinstance(self.text, str):
            raise TypeError("Internal storage must be a string.")
        return self.text

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    samples = [
        "hello world",
        "HELLO WORLD",
        "Hello World!",
        "  python is great  ",
        ""
    ]

    print("String Case Manipulator Demo")
    print("-" * 30)

    for sample in samples:
        manipulator = StringCaseManipulator(sample)
        
        current_state = manipulator.get_current()
        lower_result = manipulator.to_lower()
        upper_result = manipulator.to_upper()
        title_result = manipulator.to_title()

        print(f"Original Input: '{current_state}'")
        print(f"Lowercase:     '{lower_result}'")
        print(f"Uppercase:     '{upper_result}'")
        print(f"Title Case:    '{title_result}'")
        
        # Optional demonstration of state persistence if needed, 
        # though the design keeps original text immutable per instance logic above.
        # If we wanted to update internal state, it would require a setter method not requested here.
        
        print("-" * 30)