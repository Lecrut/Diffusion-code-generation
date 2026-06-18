class StringAssembler:
    def join_parts(self, parts: list[str], separator: str = ' ', fill_value: str = '') -> str:
        """
        Efficiently builds a string from a list of parts using the built-in str.join().
        
        Args:
            parts (list[str]): List of strings to be joined.
            separator (str): String to insert between elements in the list. Default is ' '.
            fill_value (str): Value used if an element in the list is empty or None, 
                              though typically str.join handles non-empty strings well.
        
        Returns:
            str: The resulting concatenated string with separators inserted.
        """
        # Filter out elements that are effectively "empty" based on fill_value logic if needed,
        # but standard join works best with a clean list of actual parts to avoid 
        # unexpected behavior with empty strings vs None/missing values unless specified otherwise.
        # Given the requirement for maximum performance and simplicity using built-ins:
        
        # If fill_value is provided and we need to handle potential gaps, we could filter or replace,
        # but standard join expects a list of items. The most robust simple approach 
        # that leverages str.join directly without extra loops (which are slower in Python)
        # assumes 'parts' contains the actual string segments. If fill_value implies replacing empty strings:
        
        clean_parts = [p if p else fill_value for p in parts]
        return separator.join(clean_parts)

if __name__ == '__main__':
    assembler = StringAssembler()

    sample1 = ["Hello", "World"]
    result1 = assembler.join_parts(sample1, separator=',')
    
    sample2 = ["Python", "", "is", None]
    # Assuming fill_value replaces empty/None-like gaps with a placeholder if intended behavior
    # However, standard join on ['a', '', 'b'] gives 'a b'. 
    # If the intent is to replace empty strings specifically:
    
    result2 = assembler.join_parts(sample2, separator='-', fill_value='<missing>')

    print(f"Joined Sample 1 ({sample1}): '{result1}'")
    print(f"Joined Sample 2 ({sample2}, fill='{assembler.__init__.__code__.co_varnames[0] if hasattr(assembler.__init__, '__code__') else ''}') -> {fill_value}: '{result2}'")

    # Corrected simple usage for clarity in the block:
    sample3 = ["First", "Second"]
    result3 = assembler.join_parts(sample3, separator=' | ')
    
    print(f"Joined Sample 3 ({sample3}): '{result3}'")