class StringBuilder:
    def __init__(self):
        """Initialize an empty string."""
        self._buffer = []

    def append_and_join(self, parts: list[str], separator: str) -> str:
        """
        Appends the given parts to the internal buffer and returns a new joined string.
        
        The method appends each part from 'parts' into its own entry in the buffer.
        It then constructs a single result string by joining all entries (existing 
        plus newly appended) with the provided separator, returning this final formatted string.
        """
        self._buffer.extend(parts)
        return separator.join(self._buffer)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    sb = StringBuilder()

    result1 = sb.append_and_join(["Hello", "World"], ", ")
    print(f"Result 1: '{result1}'")

    # Append more parts and join again with a different separator
    result2 = sb.append_and_join(["Python", "is", "great"], "")
    print(f"Result 2 (with empty sep): '{result2}'")

    # Final demonstration combining previous state with new data
    final_result = sb.append_and_join(["!", "."], "- ")
    print(f"Final Result: '{final_result}'")