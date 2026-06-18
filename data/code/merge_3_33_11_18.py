class StringCleaner:
    """A class to clean strings by removing all spaces."""

    def __init__(self):
        self._instance_name = "StringCleaner"

    def clean(self, text: str) -> str:
        """
        Removes all space characters from the input string.
        
        This method is optimized for performance on large strings using list comprehension 
        and joining, which typically outperforms repeated slicing in Python's CPython implementation.
        
        Args:
            text (str): The input string containing spaces to be removed.
            
        Returns:
            str: A new string with all space characters (' ') removed.
            
        Raises:
            TypeError: If the input is not a string instance.
        """
        if not isinstance(text, str):
            raise TypeError(f"Expected string type, got {type(text).__name__}")

        # Convert list of non-space chars to string efficiently
        return ''.join(char for char in text if char != ' ')

if __name__ == '__main__':
    cleaner = StringCleaner()
    
    # Sample test cases
    samples = [
        "Hello World",
        "",
        "   Multiple   Spaces   Here   ",
        "NoSpacesAtAll123",
        "Special chars: ! @ # $ % ^ & * ( ) _ - = + [] {} | : \\ ; \" ' , . / ?",
    ]

    for sample in samples:
        result = cleaner.clean(sample)
        print(f"Input:  '{sample}'")
        print(f"Output: '{result}'\n")