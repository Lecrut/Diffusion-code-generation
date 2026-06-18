import string

class StringManipulator:
    """A utility class to handle various string manipulation tasks."""

    def merge_fragments(self, fragments):
        """
        Merges a list of string fragments into a single cohesive string.
        
        Parameters:
            fragments (list[str]): A list containing individual string fragments.
            
        Returns:
            str: The merged string from all fragments.
            
        Raises:
            TypeError: If the input is not a list or if it contains non-string elements.
        """
        # Validate input type and element types
        if not isinstance(fragments, list):
            raise TypeError("Input must be a list.")
        
        for idx, fragment in enumerate(fragments):
            if not isinstance(fragment, str):
                raise TypeError(f"Fragment at index {idx} is not a string.")

        # Handle the edge case where the input list is empty by returning an empty string.
        return "".join(fragments)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user interaction.
    
    # Sample 1: Normal merge with multiple fragments including a space separator logic simulation via join (default behavior).
    list_fragments = ["Hello", " ", "World"]
    result_normal = StringManipulator().merge_fragments(list_fragments)
    print(f"Normal Merge Result: '{result_normal}'")

    # Sample 2: Edge case with an empty input list.
    empty_list = []
    result_empty = StringManipulator().merge_fragments(empty_list)
    print(f"Empty List Result: '{result_empty}'")

    # Optional verification of type safety (though the main logic will raise exceptions if violated).
    try:
        invalid_input_string = "Not a list"
        StringManipulator().merge_fragments(invalid_input_string)
    except TypeError as e:
        print(f"Caught expected error for non-list input: {e}")

    # Optional verification of element type safety.
    try:
        mixed_list_with_ints = ["Text", 123, "More"]
        StringManipulator().merge_fragments(mixed_list_with_ints)
    except TypeError as e:
        print(f"Caught expected error for non-string elements: {e}")

    # Final confirmation of successful execution.
    assert result_normal == "Hello World", f"Expected 'Hello World', got '{result_normal}'"
    assert result_empty == "", f"Expected empty string, got '{result_empty}'"
    print("All assertions passed successfully.")