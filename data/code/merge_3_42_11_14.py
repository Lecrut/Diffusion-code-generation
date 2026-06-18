class StringAssembler:
    def join_parts(self, parts: list[str], separator: str = ' ', fill_value: str = '') -> str:
        """
        Efficiently joins a list of strings with a specified separator using the built-in str.join() method.
        
        Parameters:
            parts (list[str]): A list of string elements to join.
            separator (str): The string used as a delimiter between elements. Defaults to space ' '.
            fill_value (str): Used if an element in parts is None or empty, though typically str.join handles 
                             non-empty strings directly. If the task implies filling missing/empty items with this value,
                             it would require preprocessing; however, per standard join behavior and performance optimization,
                             we assume valid string inputs unless fill_value indicates replacement of specific markers (e.g., None).
        
        Returns:
            str: The resulting joined string.
        """
        # Filter out non-string items if necessary based on type hints, but here parts is strictly list[str].
        # If the requirement implies replacing empty strings or handling missing values via fill_value, 
        # we can preprocess to replace None with fill_value before joining for robustness without sacrificing join performance.
        
        processed_parts = []
        for part in parts:
            if isinstance(part, str):
                processed_parts.append(part)
            else:
                # If a non-string is encountered (though type hint says list[str]), replace with fill_value or skip? 
                # Assuming we should handle potential None by replacing with fill_value to maintain length structure.
                processed_parts.append(fill_value if part is not None and isinstance(part, str) == False else '')

        return separator.join(processed_parts)

if __name__ == '__main__':
    assembler = StringAssembler()
    
    # Hard-coded sample values ensuring no user input or external dependencies
    sample_data_1 = ['Hello', 'world!', 'Python']
    result_1 = assembler.join_parts(sample_data_1, separator=' ', fill_value='')
    
    sample_data_2 = [None, 'First item', None]
    # Here we demonstrate handling of non-string or None by using fill_value logic if needed. 
    # Since type hint is list[str], let's assume valid strings but test robustness with a custom scenario:
    result_2 = assembler.join_parts(sample_data_1, separator=', ', fill_value='[MISSING]')

    print("Sample 1 (default):", result_1)
    print("Sample 2 (custom separator and filler logic for None if applicable in real use case):")
    
    # Additional test with explicit empty strings to show behavior
    sample_data_3 = ['A', '', 'C']
    result_3 = assembler.join_parts(sample_data_3, separator=' - ', fill_value='')
    print("Sample 3 (with empty string):", result_3)

    # Final comprehensive example
    final_list = [f"Item {i}" for i in range(10)]
    final_result = assembler.join_parts(final_list, sep='-')
    print(f"\nJoined list of 10 items: '{final_result}'")