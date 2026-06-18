class StringManipulator:
    def merge_fragments(self, fragments):
        """
        Merges a list of string fragments into one cohesive string.
        
        Args:
            fragments (list[str]): A list containing the individual string parts to be merged.
            
        Returns:
            str: The concatenated result of all strings in the input list.
                 If the input list is empty, returns an empty string.
        """
        return "".join(fragments)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    # Test case 1: Normal list of fragments
    test_list_1 = ["Hello", " ", "World"]
    
    # Test case 2: Empty list (edge case)
    test_list_2 = []
    
    # Test case 3: List with single element
    test_list_3 = ["Python is great."]
    
    # Create an instance of the class and run tests
    manipulator = StringManipulator()
    
    result1 = manipulator.merge_fragments(test_list_1)
    print(f"Test 1 (Normal): '{result1}'")
    
    result2 = manipulator.merge_fragments(test_list_2)
    print(f"Test 2 (Empty List): '{result2}'")
    
    result3 = manipulator.merge_fragments(test_list_3)
    print(f"Test 3 (Single Element): '{result3}'")