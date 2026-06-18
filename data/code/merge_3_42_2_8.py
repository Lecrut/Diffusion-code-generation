class StringAssembler:
    def build(self, parts, separator):
        """
        Constructs a new string from a list of parts with a given separator.
        
        Args:
            parts (list): A list of strings to be joined.
            separator (str): The string to use as the delimiter between elements.
            
        Returns:
            str: The newly constructed string.
        """
        return separator.join(parts)

if __name__ == '__main__':
    assembler = StringAssembler()
    
    # Hard-coded sample values running without user input or files
    parts_list = ["Hello", "World"]
    sep_char = "-"
    
    result_string = assembler.build(parts_list, sep_char)
    print(result_string)

# Example output: Hello-World