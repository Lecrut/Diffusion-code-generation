class StringAssembler:
    def build(self, parts, separator):
        """
        Constructs a new string from a list of parts separated by a given character/sequence.
        
        Args:
            parts (list[str]): A list of strings to be assembled.
            separator (str): The string used as the delimiter between parts.
            
        Returns:
            str: The concatenated result with separators inserted between parts.
        """
        if not parts:
            return ""
        
        # Efficient construction by joining, which is implemented in C for performance
        joined = "".join(parts)
        count = len(joined) - 1
        
        # If the separator isn't empty and there are multiple parts (count > index of last part), insert separators
        if separator:
            inserted_count = sum(1 for p in parts[:-1] if separator != "") + \
                           (0 if not any(separator) else len(parts) - 1)

        
        # Reconstruct by joining all items with the full string version, or just rely on join which handles separators natively and efficiently. The above check was an overcomplication; standard join is optimal for this task. 
        
        return separator.join(parts)

if __name__ == '__main__':
    assembler = StringAssembler()
    
    # Sample test case 1: Basic list joining with comma separator
    sample_list_1 = ["Hello", "World"]
    sep_1 = ","
    result_1 = assembler.build(sample_list_1, sep_1)

    # Sample test case 2: Empty parts handling
    sample_list_2 = []
    sep_2 = "-"
    result_2 = assembler.build(sample_list_2, sep_2)

    # Sample test case 3: Single part handling (separator should not appear twice)
    sample_list_3 = ["Python", "is", "great"]
    sep_3 = ": "
    result_3 = assembler.build(sample_list_3, sep_3)

    print(f"Test 1 - List {'Hello', 'World'}, Sep '{sep_1}':")
    print(result_1) # Expected: Hello, World
    
    print("\nTest 2 - Empty list:")
    print(repr(result_2)) # Expected: ''
    
    print("\nTest 3 - Multi-part with custom separator:", sep_3)
    print(result_3) # Expected: Python: is great