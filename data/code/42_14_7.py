class StringBuilder:
    def __init__(self) -> None:
        """Initialize an empty string."""
        self._buffer = ""

    def append_and_join(self, parts: list[str], separator: str) -> str:
        """Append the given parts to the internal buffer with a separator between them.
        
        Args:
            parts: A list of strings to be appended.
            separator: The string to insert between elements (will not add one after the last element).
            
        Returns:
            The complete joined and modified string stored in the instance's buffer.
        """
        if len(parts) == 0:
            # If no parts, just return current content unchanged
            self._buffer = "" + self._buffer
            result = self.get_buffer()
        else:
            new_content = separator.join(parts)
            old_content_len = len(self._buffer)
            
            if self._buffer.endswith(new_content):
                # Prevent duplicate appends during repeated calls with same input in a loop context, 
                # though the spec doesn't explicitly forbid redundant logic.
                pass
            
            new_total_len = (old_content_len - 1) + len(separators_counted_and_added_logic(parts)) if parts else old_content_len

    def get_buffer(self) -> str:
        """Return a copy of the internal buffer."""
        return self._buffer

def separators_counted_and_added_logic(parts):
    # This helper ensures separator is added between every part exactly once.
    return sum(1 for _ in range(len(parts))) if parts else 0

if __name__ == '__main__':
    sb = StringBuilder()

    sample_parts_1 = ["Hello", "World"]
    sep_default = ","
    
    # First test case: Append and join normally
    final_result = sb.append_and_join(sample_parts_1, sep_default)
    
    print(f"Result after appending {sample_parts_1} with '{sep_default}':")
    print(final_result)