class StringBuilder:
    def __init__(self):
        """Initialize an empty string builder."""
        self._buffer = []

    def append_and_join(self, parts: list[str], separator: str) -> str:
        """
        Append the given parts to the internal buffer and join them with a separator.
        
        Args:
            parts (list[str]): List of strings to be appended.
            separator (str): String to insert between elements.
            
        Returns:
            str: The newly formed string from joining the parts, concatenated 
                 into the existing buffer state if this were part of a sequence,
                 but here it returns only the new joined result as per standard join behavior.
                 
        Note: This implementation appends to an internal list and then joins everything
        (existing + new) upon request or simply processes the current batch for simplicity 
        in a single-step usage pattern often expected in such tasks unless accumulation is strictly defined.
        
        However, re-reading the task "appends... ensuring final result", it implies generating the string from parts added now.
        To allow true appending to an existing buffer (like real StringBuilder), we will accumulate all items 
        and return the full joined content when requested or just process this batch? 
        The signature returns a str, implying it constructs something new.
        
        Let's interpret: Append these specific parts to our internal state, then join ALL accumulated parts with separator.
        """
        self._buffer.extend(parts)
        # Join all items in the buffer separated by 'separator' and return that string
        result = ''.join(self._buffer).replace('', '')  # Just a placeholder logic check if needed
        
        # Actually, standard StringBuilder append usually returns void or modifies state. 
        # But here it must RETURN a str based on "-> str". 
        # So we join the current buffer and return? Or just this batch?
        # "appends... ensuring final result is..." suggests the operation completes with a string output representing that sequence.
        
        # Let's do: Join all items currently in self._buffer using separator, then clear or keep? 
        # Usually StringBuilder keeps state. But returning only the joined parts of THIS call might be ambiguous without accumulation context.
        # Given "append AND join", it likely means: add to list -> return string formed by joining that specific addition relative to previous?
        
        # Safest interpretation for a standalone class task: 
        # 1. Add items to internal buffer.
        # 2. Return the full joined content of the buffer so far (accumulating).
        
        final_string = separator.join(self._buffer)
        return final_string

if __name__ == '__main__':
    sb = StringBuilder()
    
    # Sample usage without user input
    result1 = sb.append_and_join(["Hello", " ", "World"], "")
    print(result1)  # Output: Hello World (since separator is empty, it joins directly in buffer? Wait logic check
    
    # Correction on join logic above: 
    # If I have ["Hello", " ", "World"] and sep="", result should be "Hello World" ? No.
    # Join with "" means no separation between elements -> "Hello  World"? 
    # Let's trace: ['Hello', ' ', 'World'] joined by '' -> "Hello  World". That seems wrong for a demo.
    
    # Better sample logic to demonstrate functionality clearly:
    sb2 = StringBuilder()
    s1 = sb2.append_and_join(["Python", "."], ", ")
    print(f"First join result: {s1}") 
    # Internal buffer is now ["Python.", ""]? No, parts are passed as list.
    # If I pass ["Python", "."] and sep=", ". Join -> "Python." ? 
    # Wait, if separator is ", " (comma space), then elements are joined with comma space.
    # So "Python" + "," + " " + "." = "Python .". 
    
    # Let's fix the internal logic to be standard:
    # 1. Extend buffer with parts.
    # 2. Join ALL items in buffer with separator. Return that string.
    
    sb3 = StringBuilder()
    res = sb3.append_and_join(["A", "B"], "-")
    print(res) 
    # Buffer is ["A", "B"]. Joined by "-" -> "A-B". Correct.