class StringAssembler:
    def build(self, parts, separator):
        """
        Efficiently constructs a new string from a list of parts using the given separator.
        
        Args:
            parts (list[str]): A list of strings to be joined.
            separator (str): The string to insert between each part in the list.
            
        Returns:
            str: The resulting concatenated string with separators inserted correctly.
        """
        if not parts:
            return ""
        
        # Handle empty separator case efficiently by joining directly without intermediate lists for performance
        result = []
        for i, part in enumerate(parts):
            result.append(part)
            if i < len(parts) - 1 and separator != "":
                result.append(separator)
        
        return "".join(result)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies
    assembler = StringAssembler()

    test_cases = [
        ["Hello", " ", "World"],
        ["Python", "-", "is", "-amazing"],
        [],
        ["Single"],
        ["Part1", "", "Part2"]  # Empty separator case
    ]

    for parts in test_cases:
        output = assembler.build(parts, "") if len(parts) == 0 else assembler.build(parts, ", ")
        print(f"Input: {parts}")
        print(f"Output: '{output}'")