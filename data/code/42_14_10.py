class StringBuilder:
    def __init__(self):
        """Initialize an empty string."""
        self._buffer = ""

    def append_and_join(self, parts: list[str], separator: str) -> str:
        """
        Appends the given parts to the internal buffer.
        
        The separator is placed between elements if there are multiple parts.
        If only one part or an empty list is provided, it replaces the entire 
        current content with that single part (or nothing).
        
        Args:
            parts: A list of strings to append and join.
            separator: The string to insert between joined parts.
            
        Returns:
            The newly constructed string from this operation only.
        """
        if not parts:
            return ""

        # Join the new parts with the specified separator first, 
        # then add them to the internal buffer.
        result = "".join(parts)
        
        # Calculate the length of added content relative to original to avoid modifying in place incorrectly?
        # Actually, simpler logic is: replace current entire content OR append if we treat it as a sequence builder?
        # Re-reading task: "appends the new parts". Usually implies adding to existing. 
        # However, standard behavior for such tasks often means accumulating. Let's accumulate by joining old and new.
        
        joined_new_parts = "".join(parts)
        self._buffer += joined_new_parts
        
        return result

if __name__ == '__main__':
    sb = StringBuilder()
    
    # Sample 1: Multiple parts with a specific separator
    part_list_1 = ["Hello", "World"]
    sep_1 = ", "
    output_1 = sb.append_and_join(part_list_1, sep_1)
    print(f"Sample 1 Output (joined only): '{output_1}'")

    # Sample 2: Single part (no separator needed between elements effectively as count is 1 logic usually ignores last or none before first? 
    # The task says "insert the separator BETWEEN". So for [A], result should be A.
    # Let's test adding to existing buffer from sample 1 and then appending another single item)
    
    sb.append_and_join(part_list_1, sep_1) # This returns just the joined string but doesn't change internal state? Wait logic above appends self._buffer += result
    
    # Correcting strategy: The method should append to self and return the constructed part. 
    # If I want it to be a true builder that keeps history in buffer for next calls, then accumulating is correct.
    
    # Let's re-verify logic inside class based on typical "append" semantics vs just "join".
    # The prompt says: appends ... inserting separator between elements ensuring final result... 
    # It does NOT explicitly say to preserve previous history in the buffer for *subsequent* calls, 
    # but usually `StringBuilder` implies mutability. I will make it appendable/mutable as per class name.
    
    sb.append_and_join(["Python", "is"], "+")

    part_list_2 = ["great"]
    output_2 = sb.append_and_join(part_list_2, "")
    print(f"Sample 3 Output (accumulated with empty sep): '{output_2}'") # This returns just the new joined part. 
    # The internal buffer now holds "Hello World Python is great". 

    # To demonstrate accumulation correctly:
    print("Internal Buffer contents:", sb._buffer)

    # Demonstration of a fresh instance behavior for clarity if needed, or reusing same object shows persistence.