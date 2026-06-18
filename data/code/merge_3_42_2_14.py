class StringAssembler:
    def build(self, parts, separator):
        """
        Efficiently constructs a new string from input list of parts and a chosen separator.
        
        Args:
            parts (list): A list of strings to be joined.
            separator (str): The string to insert between each part in the list.
            
        Returns:
            str: The resulting concatenated string with separators inserted.
        """
        if not parts:
            return ""
        
        # Handle edge case where there's only one item or an empty list efficiently
        result = "".join(parts[:1])
        
        for i in range(1, len(parts)):
            result += separator + parts[i]
            
        return result

if __name__ == '__main__':
    assembler = StringAssembler()
    
    # Hard-coded sample values to test the functionality
    sample_parts = ["Hello", "World"]
    sep_a = "-"
    output1 = assembler.build(sample_parts, sep_a)
    
    sample_parts2 = ["Python", "is", "great"]
    sep_b = ""
    output2 = assembler.build(sample_parts2, sep_b)
    
    print(f"Sample 1 (separator '-'): '{output1}'")
    print(f"Sample 2 (separator ''): '{output2}'")