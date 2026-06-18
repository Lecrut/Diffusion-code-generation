class StringBuilder:
    def __init__(self):
        """Initialize an empty string builder."""
        self._string = ""

    def append_and_join(self, parts: list[str], separator: str) -> str:
        """
        Appends the given parts to the internal string with a separator between them.
        
        Args:
            parts (list[str]): A list of strings to be appended and joined.
            separator (str): The string to insert between elements in 'parts'.
            
        Returns:
            str: The newly formed concatenated string from the current state plus new parts.
        """
        # Join the new parts with the separator first, then append to internal buffer
        new_content = separator.join(parts)
        self._string += new_content
        return self._string

if __name__ == '__main__':
    # Sample usage without any user input or external dependencies
    sb = StringBuilder()

    result1 = sb.append_and_join(["Hello", "World"], ", ")
    
    result2 = sb.append_and_join(
        ["This is a test.", "It works!"], 
        "|"
    )

    print("Result 1:", result1)
    print("Final String Builder Content:", sb._string)