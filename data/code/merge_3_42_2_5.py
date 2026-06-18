class StringAssembler:
    def build(self, parts, separator):
        """
        Efficiently constructs a new string from a list of parts using a specified separator.
        
        Args:
            parts (list[str]): A list of strings to be joined.
            separator (str): The string used as the delimiter between elements in 'parts'.
            
        Returns:
            str: The constructed string with separators placed between each part.
        """
        if not parts:
            return ""
        
        # Using a generator expression within join is efficient for large lists 
        # because it avoids creating intermediate list objects during the joining process.
        result = separator.join(parts)
        return result

if __name__ == '__main__':
    assembler = StringAssembler()

    sample_parts_1 = ["Hello", "World"]
    sep_1 = ", "
    
    sample_parts_2 = ["Python", "is", "great"]
    sep_2 = "-"
    
    # Test case 1: Simple join with comma and space
    output_1 = assembler.build(sample_parts_1, sep_1)
    
    # Test case 2: Join multiple words with hyphen
    output_2 = assembler.build(sample_parts_2, sep_2)

    print("Output 1:", repr(output_1))
    print("Output 2:", repr(output_2))