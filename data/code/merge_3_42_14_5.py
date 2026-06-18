class StringBuilder:
    def __init__(self) -> None:
        """Initialize an empty string."""
        self._buffer = ""

    def append_and_join(self, parts: list[str], separator: str) -> str:
        """
        Appends the new parts to the internal string and returns them joined.
        
        Args:
            parts (list[str]): A list of strings to be appended and joined.
            separator (str): The string to insert between elements.
            
        Returns:
            str: The concatenated result after appending, but NOT added back 
                 to the internal buffer unless explicitly modified elsewhere.
                 Based on the requirement "appends... correctly inserting", 
                 we interpret this as performing a single append-and-return operation 
                 without permanently modifying self._buffer if not specified otherwise.
                 However, standard practice for builders is accumulation. 
                 Given "append ... to the internal string", let's accumulate it.
        """
        # Join parts with separator in-place or create new and return?
        # The signature implies a method that appends AND returns something?
        # Usually builder appenders modify state silently, but this one asks for `-> str`.
        # If we must append to internal buffer, let's do:
        
        current_length = len(self._buffer) + (len(parts)) * 10  # heuristic estimate
        
        if not parts and separator == "":
            return ""

        joined_parts = separator.join(map(str, parts))
        
        new_buffer_content = self._buffer + joined_parts
        self._buffer = new_buffer_content
        return new_buffer_content

if __name__ == '__main__':
    # Sample usage hard-coded to run without input
    
    sb1 = StringBuilder()
    result1 = sb1.append_and_join(["Hello", "World"], " ")
    
    print("Test 1 (Basic append and join):")
    print(f"Result: {result1}")
    assert " Hello World" in result1 or result1 == r" Hello World", f"Expected joined string, got {result1}"

    # Second test adding more parts later
    sb2 = StringBuilder()
    part_a = ["App"]
    res_parta = sb2.append_and_join(part_a, "_")
    
    part_b = ["le", "net"]
    final_res = sb2.append_and_join(part_b, "")
    
    print("\nTest 2 (Multiple calls and empty separator):")
    print(f"After first call: {res_parta}")
    print(f"Final result after second call with '' sep: '{final_res}'")

    # Test with special chars in parts/separator
    sb3 = StringBuilder()
    test_parts = ["One", "2+=", "Three"]
    final_sep = "+=" + "=" * 50
    
    res_final = sb3.append_and_join(test_parts, final_sep)
    
    print("\nTest 3 (Special characters and separator length):")
    print(f"Result: {res_final}")