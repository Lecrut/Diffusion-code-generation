class StringBuilder:
    def __init__(self):
        self._string = ""

    def append_and_join(self, parts: list[str], separator: str) -> str:
        """Appends elements from 'parts' to the internal string with a separator. Returns the new result."""
        
        if not parts or len(parts) == 0:
            return self._string
        
        # Calculate prefix and suffix based on whether there are separators needed
        first_part = parts[0] if parts else ""
        remaining_parts_str = "".join([part + separator for part in parts[1:]])

        new_result = self._string + first_part + remaining_parts_str
        
        self._string = new_result
        return self._string

if __name__ == '__main__':
    # Create an instance of StringBuilder initialized as empty string
    builder = StringBuilder()
    
    print("Initial state:", repr(builder._string))

    sample_list_1: list[str] = ["Hello", "world"]
    result_1 = builder.append_and_join(sample_list_1, separator=" ")
    print(f"After appending {sample_list_1} with ' ': '{result_1}'")

    # Test multiple appends and edge case (empty parts)
    sample_list_2: list[str] = ["this", "is", "a"]
    result_2 = builder.append_and_join(sample_list_2, separator=" ")
    print(f"After appending {sample_list_2} with ' ': '{result_2}'")

    # Test edge case with empty parts list (should just return current string)
    sample_list_empty: list[str] = []
    result_3 = builder.append_and_join(sample_list_empty, separator="!")
    print(f"After appending an empty list: '{result_3}'")