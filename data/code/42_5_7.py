class StringManipulator:
    def merge_fragments(self, fragments):
        """
        Merges a list of string fragments into one cohesive string.
        
        Args:
            fragments (list[str]): A list of strings to be merged.
            
        Returns:
            str: The concatenated result or an empty string if the input is None/empty.
        """
        # Handle edge case where input might not be a proper list or is empty
        if not isinstance(fragments, list):
            return ""
        
        if len(fragments) == 0:
            return ""
            
        return "".join(fragments)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_cases = [
        ["Hello", " ", "World"],
        [],
        ["Single"],
        None,  # Should handle non-list gracefully based on docstring logic or raise if strict type check needed (current implementation returns empty)
        ["Part1", "", "Part3"]  # Empty string in middle should be preserved as join behavior does it naturally unless filtered
    ]

    manipulator = StringManipulator()

    for i, case in enumerate(test_cases):
        try:
            result = manipulator.merge_fragments(case) if isinstance(case, list) else ""
            print(f"Test Case {i + 1}: Input={case}, Output='{result}'")
        except Exception as e:
            print(f"Test Case {i + 1} Error: {e}")