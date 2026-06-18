class StringAssembler:
    def build(self, parts, separator):
        """
        Efficiently constructs a new string from the input list of parts 
        using the specified separator between each part.
        
        Args:
            parts (list[str]): A list of strings to be joined.
            separator (str): The string to insert between elements in the list.
            
        Returns:
            str: The constructed string with separators placed correctly.
        """
        if not parts:
            return ""
        
        # Using a generator expression within join is efficient for large lists 
        # as it avoids creating intermediate lists of strings.
        return separator.join(parts)

if __name__ == '__main__':
    assembler = StringAssembler()
    
    sample_parts_1 = ["Hello", "World"]
    sample_separator_1 = ", "
    result_1 = assembler.build(sample_parts_1, sample_separator_1)
    print(f"Result 1: '{result_1}'")

    sample_parts_2 = ["Python", "is", "powerful", "!"]
    sample_separator_2 = "-"
    result_2 = assembler.build(sample_parts_2, sample_separator_2)
    print(f"Result 2: '{result_2}'")

    empty_list_result = assembler.build([], ", ")
    print(f"Empty list result: '{empty_list_result}'")