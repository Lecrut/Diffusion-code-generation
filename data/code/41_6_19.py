class StringCaseManager:
    """A class to efficiently manipulate string cases."""

    def lower(self, text):
        """Converts all characters in the string to lowercase."""
        return str(text).lower() if isinstance(text, (str, bytes)) else ""

    def upper(self, text):
        """Converts all characters in the string to uppercase."""
        return str(text).upper() if isinstance(text, (str, bytes)) else ""

    def title(self, text):
        """Capitalizes each word in the string."""
        # Split by whitespace, capitalize each part, then join back.
        words = []
        for word in str(text).split():
            if not word:
                continue
            new_word = ''.join(c.capitalize() for c in word)
            words.append(new_word)
        return ' '.join(words)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    test_string = "hello world this is a python example"

    manager = StringCaseManager()

    print("Original:", test_string)
    print("Lowercase: ", manager.lower(test_string))
    print("Uppercase: ", manager.upper(test_string))
    print("Title Case: ", manager.title(test_string))