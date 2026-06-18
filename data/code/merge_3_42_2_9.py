class StringAssembler:
    def build(self, parts, separator):
        """
        Efficiently constructs a new string from the input list of parts 
        separated by the specified character/string.
        
        Args:
            parts (list): A list of strings to be joined.
            separator (str): The string used as a delimiter between items in the list.
            
        Returns:
            str: The resulting concatenated string with separators inserted.
        """
        if not parts:
            return ""
        
        # Using itertools.chain is efficient for large lists but requires import, 
        # so we use the built-in join which is highly optimized in CPython (O(n)).
        result = separator.join(parts)
        return result

if __name__ == '__main__':
    assembler = StringAssembler()
    
    sample_list_1 = ["Hello", "World"]
    sep_1 = ", "
    output_1 = assembler.build(sample_list_1, sep_1)
    
    sample_list_2 = []
    sep_2 = "|"
    output_2 = assembler.build(sample_list_2, sep_2)
    
    print("Sample 1 Output:", repr(output_1))
    print("Sample 2 Output:", repr(output_2))