class StringManipulator:
    """A utility class for string manipulation tasks."""

    def merge_fragments(self, fragments):
        """
        Merges a list of string fragments into one cohesive string.
        
        Handles edge cases where the input list is empty by returning an empty string.
        
        Args:
            fragments (list[str]): A list containing individual string parts to be merged.
            
        Returns:
            str: The concatenated result of all strings in the list, or an empty string if the list is empty.
        """
        return "".join(fragments)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_cases = [
        ["Hello", " ", "World"],
        [],
        ["Python", "-", "is", "-"],
        ["Single"]
    ]

    manipulator = StringManipulator()

    for i, fragments in enumerate(sample_cases):
        result = manipulator.merge_fragments(fragments)
        print(f"Input: {fragments}")
        print(f"Merged Result: '{result}'")
        print("-" * 20)