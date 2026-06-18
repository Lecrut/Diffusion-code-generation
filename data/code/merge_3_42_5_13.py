class StringManipulator:
    def merge_fragments(self, fragments):
        """
        Merges a list of string fragments into a single cohesive string.
        
        Args:
            fragments (list[str]): A list containing the individual strings to be merged.
            
        Returns:
            str: The concatenated result of all fragments in order. 
                 If the input list is empty, returns an empty string.
        """
        return "".join(fragments)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or args)
    
    # Test case 1: Normal list of fragments
    test_fragments_01 = ["Hello", " ", "World"]
    
    # Test case 2: Empty list (edge case)
    test_fragments_02 = []
    
    # Instantiate the class and apply the method to both cases
    manipulator = StringManipulator()
    
    result_case_1 = manipulator.merge_fragments(test_fragments_01)
    print("Test Case 1 (Normal):")
    print(f"Input: {test_fragments_01}")
    print(f"Merged Result: '{result_case_1}'\n")
    
    result_case_2 = manipulator.merge_fragments(test_fragments_02)
    print("Test Case 2 (Empty List):")
    print(f"Input: {test_fragments_02}")
    print(f"Merged Result: '{result_case_2}'\n")

# Final confirmation that both samples executed successfully without errors.