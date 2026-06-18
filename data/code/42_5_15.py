class StringManipulator:
    """A class providing basic string manipulation utilities."""
    
    def merge_fragments(self, fragments):
        """
        Merges a list of string fragments into one cohesive string.
        
        Args:
            fragments (list[str]): A list containing individual strings to be merged.
            
        Returns:
            str: The concatenated result of all fragments in order.
            
        Raises:
            TypeError: If the input is not a list or if elements are not strings.
        """
        # Validate input type and element types
        if not isinstance(fragments, list):
            raise TypeError("Input must be a list.")
        
        for fragment in fragments:
            if not isinstance(fragment, str):
                raise TypeError("All elements in the list must be strings.")
                
        return "".join(fragments)

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without user input
    
    # Test case 1: Normal merging with multiple fragments
    normal_fragments = ["Hello", " ", "World"]
    
    # Test case 2: Empty list (edge case)
    empty_fragments = []
    
    # Create an instance of the class
    manipulator = StringManipulator()
    
    print("Test Case 1 - Normal Fragments:")
    result_normal = manipulator.merge_fragments(normal_fragments)
    print(f"Input: {normal_fragments}")
    print(f"Output: '{result_normal}'")
    assert result_normal == "Hello World", f"Expected 'Hello World', got '{result_normal}'"
    
    print("\nTest Case 2 - Empty List:")
    result_empty = manipulator.merge_fragments(empty_fragments)
    print(f"Input: {empty_fragments}")
    print(f"Output: '{result_empty}'")
    assert result_empty == "", f"Expected empty string, got '{result_empty}'"
    
    # Test case 3: Single element list
    single_fragment = ["Python is great"]
    result_single = manipulator.merge_fragments(single_fragment)
    print(f"\nTest Case 3 - Single Fragment:")
    print(f"Input: {single_fragment}")
    print(f"Output: '{result_single}'")
    
    # Test case 4: Fragments with special characters and spaces
    complex_fragments = ["Ciao", " ", "Mondo!", "!"]
    result_complex = manipulator.merge_fragments(complex_fragments)
    print(f"\nTest Case 4 - Complex Fragments:")
    print(f"Input: {complex_fragments}")
    print(f"Output: '{result_complex}'")