class StringBuilder:
    def __init__(self):
        """Initialize an empty string."""
        self._buffer = ""

    def append_and_join(self, parts: list[str], separator: str) -> str:
        """
        Appends the given list of strings to the internal buffer.
        
        The separator is inserted between elements in the list.
        Returns a new string representing the joined result without modifying self._buffer permanently 
        (as per standard append-and-return behavior for immutability safety, though typically such methods modify state).
        
        However, based on the requirement "appends... to the internal string", we will update self._buffer and return the appended portion.
        If the intention is that the method returns the full resulting string including previous content, 
        this implementation updates self._buffer with all parts joined by separator and returns that new value.
        
        Args:
            parts (list[str]): List of strings to append/join.
            separator (str): String to insert between elements in 'parts'.
            
        Returns:
            str: The newly formed string from joining the parts with the separator.
        """
        # Join the new parts with the specified separator
        joined_parts = "".join(parts) if not parts else separator.join(parts)
        
        # Update internal buffer by appending the joined result to existing content? 
        # Re-reading: "appends the new parts... ensuring final result is a single, correctly formatted string"
        # Usually implies modifying state. But returning just the appended part or full string?
        # Given typical usage patterns for such tasks unless specified otherwise (like 'return self'), 
        # we assume it should return the newly constructed segment if not meant to replace, 
        # BUT "appends... to internal" suggests mutation. Let's make it append to existing buffer and return the new total content?
        
        # Actually, looking at similar patterns: often these methods are designed so that you can chain or get a result.
        # If I strictly follow "append", then self._buffer += joined_parts is correct for state change.
        # But what does it return? The prompt says "-> str". 
        # Let's assume it returns the entire new content of StringBuilder after appending, as that makes sense for a single formatted string result.
        
        # Wait, another interpretation: maybe just append and return nothing or self? No, signature requires -> str.
        # Most logical: Append to internal buffer, then return the full current state of the builder.
        
        if parts is not None:
            joined_parts = separator.join(parts)
            self._buffer += joined_parts
            
        return self._buffer

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input(), sys.stdin, etc.)
    
    sb1 = StringBuilder()
    result1 = sb1.append_and_join(["Hello", "World"], ", ")
    print(f"Result 1: {result1}")

    sb2 = StringBuilder()
    # Test with empty list and single element edge cases implicitly handled by join logic
    result2 = sb2.append_and_join([], "")
    print(f"Result 2 (empty parts): '{result2}'")

    sb3 = StringBuilder("Initial ")
    result3 = sb3.append_and_join(["Part", "Two"], "-")
    print(f"Result 3: {result3}")