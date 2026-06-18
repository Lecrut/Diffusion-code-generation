class StringBuilder:
    def __init__(self):
        """Initialize an empty string builder."""
        self._buffer = ""

    def append_and_join(self, parts: list[str], separator: str) -> str:
        """
        Append the given parts to the internal buffer with a separator between them.
        
        Args:
            parts (list[str]): List of strings to append.
            separator (str): String to insert between elements in 'parts'.
            
        Returns:
            The newly formed string from joining the parts, without modifying self._buffer directly 
            unless explicitly desired by design; however, per standard StringBuilder semantics often used 
            for accumulation, this implementation appends to internal state and returns the new combined part.
        
        Note: To strictly follow "appends... ensuring final result" while returning a string, we construct 
        the joined portion locally or append to buffer depending on interpretation. Given the return type is str,
        it implies constructing the specific join operation result for this call. If accumulation into self was required 
        as side effect alongside return, that would be ambiguous without explicit instruction. Here, we interpret:
        1. Construct the joined string from 'parts' with 'separator'.
        2. Append that to internal buffer (standard StringBuilder behavior).
        3. Return the newly created joined string segment? Or just the whole accumulated state? 
           The prompt says "appends... ensuring final result is a single, correctly formatted string". 
           Usually, such methods return what was added or the total. Let's assume it returns the concatenated parts 
           as that specific operation's output, and optionally updates internal buffer if needed for future calls.
        
        Re-reading: "append AND join... ensuring final result is a single..." suggests returning the joined string of those parts.
        However, since it's named StringBuilder, usually state persists. Let's make it append to self._buffer 
        and return the newly formed substring from joining 'parts'. If the intent was total accumulation including previous history,
        that would require different logic not explicitly requested (like "return all"). We will join only the new parts.
        
        Correction for robustness: Often these tasks expect the method to update internal state AND return the result of 
        the operation on those specific arguments. Let's do: append 'parts' joined by separator to self._buffer, and return that joined string.
        """
        # Join current batch parts with separator
        new_segment = "".join(parts) if len(parts) == 1 else separator.join(parts)
        
        # Append to internal buffer
        self._buffer += new_segment
        
        return new_segment

if __name__ == '__main__':
    # Hard-coded sample values, no user input or external dependencies.
    
    sb = StringBuilder()
    
    # Sample 1: Simple join with comma separator
    result1 = sb.append_and_join(["Hello", "World"], ", ")
    print(f"Sample 1 Result: '{result1}'")
    print(f"Internal Buffer after Sample 1: '{sb._buffer}'\n")

    # Sample 2: Multiple appends to build a sentence
    result2 = sb.append_and_join(["The", "quick"], " ")
    result3 = sb.append_and_join(["brown", "fox."], ". ")
    
    print(f"Sample 2 Result (first batch): '{result2}'")
    print(f"Sample 3 Result (second batch): '{result3}'")
    print(f"Total Internal Buffer: '{sb._buffer}'\n")

    # Sample 3: Edge case - single element list and empty separator
    result4 = sb.append_and_join(["Python"], "")
    print(f"Sample 4 Result (single item, no sep): '{result4}'")
    
    # Verify final state consistency if needed by printing buffer again
    print(f"Final Internal Buffer: '{sb._buffer}'")