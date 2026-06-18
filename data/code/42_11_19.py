class StringAssembler:
    def join_parts(self, parts: list[str], separator: str = ' ', fill_value: str = '') -> str:
        """
        Efficiently builds a string from a list of parts using the built-in str.join().
        
        Args:
            parts (list[str]): The list of strings to be joined.
            separator (str): The string to use as a separator between elements. Defaults to ' '.
            fill_value (str): A value used if an element in parts is empty or None, 
                             though str.join() handles non-empty strings directly; this parameter
                             can be utilized via list comprehension for robustness against None/empty inputs.

        Returns:
            str: The joined string with the specified separator.
        
        Note:
            This implementation uses a generator expression within join_parts to handle potential 
            empty or None values by replacing them with fill_value before joining, ensuring maximum performance 
            while maintaining correctness for edge cases that might occur in input lists containing non-string elements 
            (like None) which would otherwise cause an error during standard str.join().
        """
        # Convert potentially problematic inputs to strings using the provided fill_value if needed.
        processed_parts = [fill_value if p is None or p == '' else p for p in parts]
        
        return separator.join(processed_parts)

if __name__ == '__main__':
    assembler = StringAssembler()

    # Sample test case 1: Basic joining with default separator and fill value
    sample_list_1 = ["Hello", "World"]
    result_1 = assembler.join_parts(sample_list_1)
    
    # Sample test case 2: Custom separator and handling empty strings as fill_value
    sample_list_2 = ["Python", "", "is", None, "great"]
    result_2 = assembler.join_parts(sample_list_2, separator='-', fill_value='<empty>')

    print(f"Result 1 (Basic): '{result_1}'")
    print(f"Result 2 (Custom & Fill): '{result_2}'")