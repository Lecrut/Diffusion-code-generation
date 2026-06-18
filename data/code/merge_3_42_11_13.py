class StringAssembler:
    def join_parts(self, parts: list[str], separator: str = ' ', fill_value: str = '') -> str:
        """
        Efficiently builds a string from a list of parts using the built-in str.join().
        
        Args:
            parts (list[str]): List of strings to be joined.
            separator (str): String used as delimiter between elements in 'parts'. Defaults to space.
            fill_value (str): Value used if an element in 'parts' is empty or None, 
                              though str.join() handles non-empty strings directly; this parameter
                              can be utilized for post-processing or validation logic if needed,
                              but the core joining relies on separator and parts content.

        Returns:
            str: The joined string with elements separated by 'separator'.
        
        Note:
            This implementation leverages Python's highly optimized C-level 
            implementation of list.join() which is significantly faster than manual loops.
        """
        # Filter out None values if necessary, or handle empty strings based on fill_value logic here if required.
        # However, the prompt specifically asks to utilize str.join(). The most direct and efficient way
        # is to pass parts directly. If 'fill_value' implies replacing specific elements (like empty ones),
        # we can preprocess, but standard join handles non-empty strings best. 
        # Assuming fill_value might be intended for handling None or empty string replacement before joining:
        
        processed_parts = []
        for part in parts:
            if isinstance(part, str) and len(part.strip()) == 0:
                # Replace stripped empty strings with fill_value if provided, otherwise keep as is (empty string joins to nothing)
                if fill_value != '' or not fill_value: 
                    processed_parts.append(fill_value)
                else:
                    processed_parts.append('')
            elif part is None and fill_value != '':
                 # If a specific element was intended to be replaced by fill_value when it's None/empty logic applies differently, handle here.
                 # For simplicity in this optimized join context without complex filtering rules defined beyond the prompt:
                 processed_parts.append(fill_value) if part is not None else '' 
            elif isinstance(part, str):
                processed_parts.append(part)
        
        return separator.join(processed_parts)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies.
    assembler = StringAssembler()

    test_cases = [
        {
            "parts": ["Hello", "", "World"],
            "separator": "-",
            "fill_value": ""
        },
        {
            "parts": ["Python", "is", "fast"],
            "separator": ", ",
            "fill_value": "[MISSING]"
        },
        {
            "parts": [],
            "separator": "|",
            "fill_value": "-"
        }
    ]

    for i, case in enumerate(test_cases):
        result = assembler.join_parts(
            parts=case["parts"], 
            separator=case["separator"], 
            fill_value=case["fill_value"]
        )
        print(f"Test Case {i + 1}:")
        print(f"Input Parts: {case['parts']}")
        print(f"Separator: '{case['separator']}'")
        print(f"Fill Value: '{case['fill_value']}'")
        print(f"Result: \"{result}\"")
        print("-" * 30)