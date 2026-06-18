class StringAssembler:
    def join_parts(self, parts: list[str], separator: str = ' ', fill_value: str = '') -> str:
        """
        Efficiently builds a string from a list of parts using the built-in str.join() method.
        
        Args:
            parts (list[str]): The list of strings to join.
            separator (str): The string to use as a separator between elements. Defaults to ' '.
            fill_value (str): A value used if an element in parts is empty or None, replacing it before joining. 
                              This prevents unwanted separators from appearing due to consecutive empty items 
                              being treated as single units by join() unless explicitly handled differently here.
        
        Returns:
            str: The joined string with elements separated by the separator and fill_value used appropriately.
        """
        # Pre-process parts to replace any occurrence of an empty or None-like part (if needed)
        if not isinstance(parts, list):
            raise TypeError("parts must be a list")

        processed_parts = []
        for p in parts:
            val = fill_value if p == '' else str(p)
            if val != '': 
                # Ensure we don't add empty strings unless they were originally non-empty but became valueless?
                pass
            
            # We will handle the logic such that any part considered "empty" (original string is '') becomes filled.
            processed_parts.append(val)

        return separator.join(processed_parts)

if __name__ == '__main__':
    assembler = StringAssembler()
    
    sample_1 = ["Hello", "", "World"]
    result_1 = assembler.join_parts(sample_1, fill_value="!")
    print(f"Sample 1: {result_1}")

    sample_2 = ["Python", "is", "fun"]
    result_2 = assembler.join_parts(sample_2)
    print(f"Sample 2: {result_2}")

    sample_3 = ["" , "", "" ]
    result_3 = assembler.join_parts(sample_3, fill_value="X")
    print(f"Sample 3: {result_3}")