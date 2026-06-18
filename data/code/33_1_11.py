import time

class StringProcessor:
    """A class to process strings with optimized operations."""

    def remove_spaces(self, input_string):
        """
        Removes all spaces from the input string in O(n) time complexity.
        
        Args:
            input_string (str): The string from which spaces should be removed.
            
        Returns:
            str: A new string with all spaces removed.
        """
        result = []
        for char in input_string:
            if char != ' ':
                result.append(char)
        return ''.join(result)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input is required
    test_cases = [
        "Hello World",
        "  Multiple   Spaces  ",
        "",
        "NoSpacesHere!",
        "A B C D E"
    ]

    processor = StringProcessor()

    for i, test_input in enumerate(test_cases):
        start_time = time.perf_counter()
        processed_output = processor.remove_spaces(test_input)
        end_time = time.perf_counter()
        
        print(f"Test Case {i + 1}:")
        print(f"Input:    '{test_input}'")
        print(f"Output:   '{processed_output}'")
        print(f"Time taken (approx): {(end_time - start_time) * 1_000_000:.2f} microseconds\n")