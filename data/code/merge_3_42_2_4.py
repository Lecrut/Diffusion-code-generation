import string

class StringAssembler:
    def build(self, parts, separator):
        """
        Efficiently constructs a new string from a list of parts using a given separator.
        
        Args:
            parts (list): A list of strings to be joined.
            separator (str): The string that separates each part in the output.
            
        Returns:
            str: The constructed string with separators placed between parts.
        """
        if not parts:
            return ""
        
        # Using join is generally efficient and optimized in Python for this use case
        result = separator.join(parts)
        return result

if __name__ == '__main__':
    assembler = StringAssembler()
    
    sample_parts_1 = ["Hello", "World"]
    sample_separator_1 = ", "
    output_1 = assembler.build(sample_parts_1, sample_separator_1)
    
    print("Sample 1 Output:")
    print(output_1)

    # Additional test cases to ensure robustness without user input
    test_cases = [
        (["Python", "is", "great"], "!"),
        ([], ""),
        (["Single"], ""),
        (["A", "B", "C", "D"], "-")
    ]

    for parts, sep in test_cases:
        result = assembler.build(parts, sep)
        print(f"Input {parts} with separator '{sep}' -> {result}")