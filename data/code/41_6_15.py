class StringCaseManipulator:
    """A class to efficiently manipulate string case formats."""

    def lower(self, s):
        """Converts a string to all lowercase letters."""
        return str(s).lower() if isinstance(s, (str, bytes)) else ""

    def upper(self, s):
        """Converts a string to all uppercase letters."""
        return str(s).upper() if isinstance(s, (str, bytes)) else ""

    def title(self, s):
        """Capitalizes the first character of each word in the string."""
        # Using join and capitalize on parts ensures correct handling of multiple spaces
        words = str(s).split(' ')
        capitalized_words = [word.capitalize() for word in words]
        return ' '.join(capitalized_words)

    def switch_case(self, s):
        """Returns a dictionary containing the string in all three common case formats."""
        if not isinstance(s, (str, bytes)):
            raise TypeError("Input must be a string.")
        
        result = {
            "lower": self.lower(str(s)),
            "upper": self.upper(str(s)),
            "title": self.title(str(s))
        }
        return result

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_strings = [
        "hello world",
        "Python Programming",
        "   multiple      spaces  ",
        ""
    ]

    manipulator = StringCaseManipulator()

    print("String Case Manipulation Results\n" + "=" * 40)
    
    for text in test_strings:
        result = manipulator.switch_case(text)
        
        original = repr(text) if len(text) > 15 else text
        print(f"\nOriginal ({original}):")
        print(f"  Lowercase : {result['lower']}")
        print(f"  Uppercase : {result['upper']}")
        print(f"  Title Case: {result['title']}")

    # Additional demonstration of individual methods on a specific string
    sample = "mixed CASE example!"
    
    print("\n" + "=" * 40)
    print("Individual Method Demonstration\n" + "=" * 40)
    print(f"\nInput: {sample}")
    print(f"Lowercase only:   '{manipulator.lower(sample)}'")
    print(f"Uppercase only:   '{manipulator.upper(sample)}'")
    print(f"Title Case only:  '{manipulator.title(sample)}'")