class StringAssembler:
    def build(self, parts, separator):
        """
        Efficiently constructs a new string from a list of parts using the specified separator.
        
        Args:
            parts (list[str]): A list of strings to be joined.
            separator (str): The string used to separate elements in the result.
            
        Returns:
            str: The constructed string with separators placed between parts.
        """
        if not parts:
            return ""
        
        # Use Python's built-in join method which is implemented in C for optimal performance
        return separator.join(parts)

if __name__ == '__main__':
    assembler = StringAssembler()
    
    sample_parts_1 = ["Hello", "World"]
    sample_separator_1 = ", "
    result_1 = assembler.build(sample_parts_1, sample_separator_1)
    print(f"Result 1: '{result_1}'")

    # Test with empty list
    result_empty = assembler.build([], "-")
    print(f"Empty List Result: '{result_empty}'")

    # Test with single element and no separator needed visually (though join handles it correctly)
    sample_parts_2 = ["Python", "is"]
    sample_separator_2 = " is "
    result_2 = assembler.build(sample_parts_2, sample_separator_2)
    print(f"Result 2: '{result_2}'")

    # Test with many parts to demonstrate efficiency compared to manual loops in large lists
    long_list = [str(i % 100) for i in range(50)]
    result_long = assembler.build(long_list, ", ")
    print(f"Long List Result Length: {len(result_long)}")