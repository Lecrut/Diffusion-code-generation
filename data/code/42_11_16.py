class StringAssembler:
    def join_parts(self, parts: list[str], separator: str = ' ', fill_value: str = '') -> str:
        """
        Efficiently builds a string from a list of parts using the built-in str.join().
        
        Args:
            parts (list[str]): A list of strings to be joined.
            separator (str): The string to use as a delimiter between elements. Defaults to ' '.
            fill_value (str): If an element in `parts` is empty, it will be replaced with this value before joining. 
                             This ensures that consecutive separators do not create unintended gaps if the original list had blanks.

        Returns:
            str: The joined string.
        """
        # Replace any existing empty strings in parts with fill_value to handle potential blank elements gracefully
        processed_parts = [fill_value if part == '' else part for part in parts]
        
        # Use built-in join method which is implemented in C and highly optimized
        return separator.join(processed_parts)

if __name__ == '__main__':
    assembler = StringAssembler()

    sample_list_1 = ["Hello", "", "World"]
    result_1 = assembler.join_parts(sample_list_1, fill_value='!')
    
    sample_list_2 = ["Python", "is", "great"]
    result_2 = assembler.join_parts(sample_list_2)
    
    print(f"Result 1 (with empty string handling): '{result_1}'")
    print(f"Result 2 (standard join): '{result_2}'")

    # Additional test with custom separator
    sample_list_3 = ["A", "B", "C"]
    result_3 = assembler.join_parts(sample_list_3, separator='-')
    print(f"Result 3 (custom separator '-'): '{result_3}'")