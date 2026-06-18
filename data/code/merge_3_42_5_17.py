import sys

class StringManipulator:
    def merge_fragments(self, fragments):
        """
        Merges a list of string fragments into one cohesive string.
        
        Args:
            fragments (list[str]): A list of strings to be merged.
            
        Returns:
            str: The merged string if the input is valid and non-empty; 
                 an empty string if the input list is empty or None.
                 
        Raises:
            TypeError: If 'fragments' is not a list containing only strings.
        """
        # Validate input type
        if not isinstance(fragments, list):
            raise TypeError("Input must be a list.")
        
        for fragment in fragments:
            if not isinstance(fragment, str):
                raise TypeError("All elements in the list must be strings.")
                
        return "".join(fragments)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or file access is needed
    
    # Test case 1: Normal operation with multiple fragments
    test_list_1 = ["Hello", " ", "World"]
    
    # Test case 2: Empty list (edge case)
    test_list_2 = []
    
    # Test case 3: Single fragment
    test_list_3 = ["Python is great."]
    
    manipulator = StringManipulator()
    
    print("Test Case 1:")
    result_1 = manipulator.merge_fragments(test_list_1)
    print(f"Input: {test_list_1}")
    print(f"Merged Result: '{result_1}'")
    print("-" * 20)
    
    print("Test Case 2 (Empty List):")
    result_2 = manipulator.merge_fragments(test_list_2)
    print(f"Input: {test_list_2}")
    print(f"Merged Result: '{result_2}'")
    print("-" * 20)
    
    print("Test Case 3 (Single Fragment):")
    result_3 = manipulator.merge_fragments(test_list_3)
    print(f"Input: {test_list_3}")
    print(f"Merged Result: '{result_3}'")