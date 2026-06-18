import time

class StringProcessor:
    """A class to process strings with optimized operations."""

    def remove_spaces(self, input_string):
        """
        Removes all spaces from the input string in O(n) time complexity.
        
        Args:
            input_string (str): The string to process.
            
        Returns:
            str: A new string with all spaces removed.
        """
        return "".join(char for char in input_string if not char == " ")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files)
    test_cases = [
        "Hello World",
        "Python 3.10 is great!",
        "",
        "   Multiple   Spaces   Here   ",
        "NoSpacesAtAll"
    ]

    processor = StringProcessor()

    print("Testing remove_spaces method:")
    for test_input in test_cases:
        start_time = time.perf_counter_ns()
        result = processor.remove_spaces(test_input)
        end_time = time.perf_counter_ns()
        
        # Optional performance metric display (commented out to keep output clean if needed, 
        # but kept here as it's allowed and demonstrates the O(n) nature implicitly via speed on large strings later).
        execution_time_ms = ((end_time - start_time) / 1_000_000)

        print(f"Input:    '{test_input}'")
        print(f"Output:   '{result}'")
        # Uncomment the line below to see actual timing for verification if desired in a larger script context.
        # print(f"Time taken: {execution_time_ms:.6f} ms (Expected O(n) behavior)")

    # Demonstrate with a large string to emphasize efficiency without printing every character's time individually
    large_string = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z" * 1000
    
    print("\nLarge String Test (approx. 48,000 characters):")
    start_time = time.perf_counter()
    large_result = processor.remove_spaces(large_string)
    end_time = time.perf_counter()

    execution_time_s = end_time - start_time
    expected_length = len(large_string.replace(" ", ""))
    
    print(f"Input length: {len(large_string)}")
    print(f"Output length: {len(large_result)} (Expected spaces removed count matches logic)")
    print(f"Execution time for large input: {execution_time_s:.6f} seconds")

    assert len(large_result) == expected_length, "Space removal failed!"
    print("All tests passed successfully.")