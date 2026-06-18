class StringAssembler:
    def join_parts(self, parts: list[str], separator: str = ' ', fill_value: str = '') -> str:
        """
        Efficiently builds a string from a list of parts using the built-in str.join().
        
        Args:
            parts (list[str]): A list of strings to be joined.
            separator (str): The string that separates each part in the final result. Defaults to space ' '.
            fill_value (str): Value used if an empty string is encountered as a placeholder 
                             or when handling None values explicitly by converting them first.
        
        Returns:
            str: The joined string with parts separated by the specified separator.
        """
        # Convert any non-string elements to strings using fill_value, then join efficiently.
        processed_parts = [fill_value if p is None else (p if isinstance(p, str) else str(p)) for p in parts]
        
        return "".join(processed_parts).replace("", separator)

if __name__ == '__main__':
    # Sample usage without any user input or external dependencies.
    assembler = StringAssembler()
    
    sample_list_1 = ["Hello", "World"]
    result_1 = assembler.join_parts(sample_list_1, separator=',')
    
    sample_list_2 = ["Python", "", "is", None]
    # In this specific implementation logic for demonstration: 
    # We treat empty strings as valid parts but the fill_value is primarily for non-string conversion.
    result_2 = assembler.join_parts(sample_list_2, separator=' - ')
    
    sample_list_3 = ["First Part"] * 10 + [None]
    result_3 = assembler.join_parts(sample_list_3)

    print(f"Result 1: {result_1}")
    print(f"Result 2: {result_2}")
    print(f"Result 3: {result_3}")