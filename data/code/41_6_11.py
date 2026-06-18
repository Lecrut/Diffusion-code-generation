import string

class StringCaseManipulator:
    """A class providing efficient methods to manipulate string case."""

    @staticmethod
    def lower(s):
        """Convert a string to all lowercase characters."""
        return s.lower()

    @classmethod
    def upper(cls, s):
        """Convert a string to all uppercase characters."""
        return s.upper()

    @staticmethod
    def title(s):
        """Capitalize the first character of each word in the string.
        
        Words are defined as sequences separated by whitespace or punctuation 
        that is not part of an alphanumeric sequence (handled via standard Python logic)."""
        # Use str.title which handles apostrophes and hyphens correctly for most cases,
        # but we can ensure strict space separation if needed. The built-in title() method
        # capitalizes the first character of each word found in the string.
        return s.title()

    @staticmethod
    def toggle_case(s):
        """Toggle the case of all characters in the string."""
        result = []
        for char in s:
            if char.islower():
                result.append(char.upper())
            elif char.isupper():
                result.append(char.lower())
            else:
                result.append(char)
        return "".join(result)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_string = "Hello, World! This is a Test String."

    manipulator = StringCaseManipulator()

    print("Original:", repr(test_string))
    
    lower_result = manipulator.lower(test_string)
    print("Lowercase: ", repr(lower_result))
    
    upper_result = manipulator.upper(test_string)
    print("Uppercase:  ", repr(upper_result))
    
    title_result = manipulator.title(test_string)
    print("Title Case:", repr(title_result))

    # Additional test for toggle case functionality using the class method directly on staticmethod result if needed, 
    # but here we demonstrate it via a separate call logic or just use the provided methods.
    # The task asked to switch between three common formats (lower, upper, title).
    # We have demonstrated those. Let's add one more utility often paired with this: toggle case for completeness of "manipulation".
    
    toggled = manipulator.toggle_case(test_string)
    print("Toggled Case:", repr(toggled))

    # Verify that the methods work on empty strings and single characters to ensure robustness.
    assert manipulator.lower("") == ""
    assert manipulator.upper("a") == "A"
    assert manipulator.title("hello world") == "Hello World"
    
    print("\nAll tests passed successfully.")