"""Utility module containing a static method to calculate string length."""

class StringUtils:
    """Provides utility functions for basic string operations."""

    @staticmethod
    def get_length(text: str) -> int:
        """
        Calculate the number of characters in the given string.

        This is equivalent to len() but encapsulated as a static method
        within this class, adhering to clean code principles.

        Args:
            text (str): The input string for which length needs to be calculated.

        Returns:
            int: The character count of the provided string.

        Raises:
            TypeError: If the input is not a string instance.
        """
        if not isinstance(text, str):
            raise TypeError("Input must be a string.")
        
        return len(text)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external inputs.
    
    test_cases = [
        "Hello, World!",
        "",
        "Python is awesome.",
        123,  # This will trigger a TypeError as expected logic check
        None, # Another type error case
    ]

    for sample in test_cases:
        try:
            length_result = StringUtils.get_length(sample)
            print(f"Input: {repr(sample)}")
            print(f"Length: {length_result}")
            print("-" * 20)
        except TypeError as te:
            print(f"Input: {repr(sample)}")
            print(f"Error (Type Error): {te}")
            print("-" * 20)