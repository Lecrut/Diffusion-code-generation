import string

class StringAssembler:
    def join_parts(self, parts: list[str], separator: str = ' ', fill_value: str = '') -> str:
        """
        Efficiently build a string from a list of parts using the built-in str.join() method.

        Parameters:
            parts (list[str]): List of strings to be joined.
            separator (str): String to insert between parts (default is ' ').
            fill_value (str): Value used if any part in the list is empty or None-like, 
                             ensuring non-empty output segments before joining (optional optimization).

        Returns:
            str: The resulting concatenated string with separators.

        Note:
            This method optimizes performance by leveraging Python's highly optimized C-implementation of str.join(),
            which avoids creating multiple intermediate strings during concatenation.
            
            If fill_value is provided and a part in the list is effectively empty or None (after stripping),
            that segment will be replaced with fill_value before joining to ensure consistent behavior.
        """
        
        # Pre-process parts: replace empty/None segments if fill_value is specified
        processed_parts = []
        for p in parts:
            stripped_p = str(p).strip() if isinstance(p, (str, bytes)) else ''

if __name__ == '__main__':
    pass
