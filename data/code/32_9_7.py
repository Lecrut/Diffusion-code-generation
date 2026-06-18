"""Utility module containing a static method to calculate string length."""

class StringUtils:
    """A utility class providing methods for common string operations."""

    @staticmethod
    def get_length(text: str) -> int:
        """
        Calculate the number of characters in the given text.

        This is equivalent to calling len() on a standard Python string,
        but encapsulated as a static method within this utility class
        for potential future extension or consistency across different types.

        Args:
            text (str): The input string whose length needs to be calculated.

        Returns:
            int: The character count of the input string.

        Raises:
            TypeError: If the input is not a string instance.
        """
        if not isinstance(text, str):
            raise TypeError(f"Expected 'str' type, got {type(text).__name__}")
        
        return len(text)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    samples = [
        "Hello, World!",
        "",
        "Python 3.x",
        "12345" * 100,
    ]

    for text in samples:
        length = StringUtils.get_length(text)
        print(f"'{text[:10]}{'...' if len(text) > 10 else ''}' has a length of {length}.")