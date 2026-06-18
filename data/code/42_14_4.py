class StringBuilder:
    def __init__(self):
        """Initialize an empty string builder."""
        self._string = ""

    def append_and_join(self, parts: list[str], separator: str) -> str:
        """
        Append the given list of strings to the internal buffer and return 
        them joined by the specified separator. The result is returned as a new 
        string; it does not modify self._string in place but accumulates 
        subsequent calls if needed (though this implementation returns fresh joins).

        Args:
            parts: A list of strings to append and join.
            separator: The string to insert between elements.

        Returns:
            A single formatted string with the joined parts.
        
        Note: This method constructs a new result based on current state 
        but for simplicity in this task, it returns the immediate concatenation 
        of all provided parts separated by the given delimiter. To maintain 
        internal consistency across multiple calls without overwriting previous content,
        we could accumulate here, but the requirement emphasizes returning "the final result".
        
        However, to strictly follow 'append' semantics while ensuring correctness:
        We will append each part (with separator handling) to self._string and return that.
        """
        # Join parts with separator immediately for this operation's output logic
        joined_result = separator.join(parts)
        
        # Append the result to internal string if we want persistent state, 
        # OR just return it as requested by "append...and join". 
        # Given the phrasing "appends the new parts", let's accumulate.
        self._string += joined_result
        
        return joined_result

if __name__ == '__main__':
    # Sample usage block with hard-coded values
    sb = StringBuilder()

    result1 = sb.append_and_join(["Hello", "World"], " ")
    
    result2 = sb.append_and_join(["This is a test.", "It works!"], ",")
    
    print("Final internal string:", repr(sb._string))