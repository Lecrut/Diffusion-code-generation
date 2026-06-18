class StringCaseManipulator:
    """A class designed to manipulate string cases."""

    def transform(self, text):
        """
        Returns a dictionary containing lowercase, uppercase, and title case versions of the input text.

        Args:
            text (str): The input string to be manipulated.

        Returns:
            dict: A dictionary with keys 'lowercase', 'uppercase', and 'title'.
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        
        return {
            "lowercase": text.lower(),
            "uppercase": text.upper(),
            "title": text.title()
        }

if __name__ == '__main__':
    manipulator = StringCaseManipulator()

    sample_text = "Hello, World! This is a Test."
    
    result = manipulator.transform(sample_text)
    
    print("Original Text:", sample_text)
    print("\nLowercase:")
    print(result["lowercase"])
    
    print("\nUppercase:")
    print(result["uppercase"])
    
    print("\nTitle Case:")
    print(result["title"])