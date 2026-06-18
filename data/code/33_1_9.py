class StringProcessor:
    """A class to process strings with optimized operations."""
    
    def remove_spaces(self, input_str):
        """
        Removes all spaces from the input string in O(n) time complexity.
        
        Args:
            input_str (str): The input string containing potential spaces.
            
        Returns:
            str: A new string with all spaces removed.
        """
        # Using replace() is efficient in Python as it typically uses C implementation,
        # but for strict algorithmic demonstration of O(n) single pass logic without built-in 
        # methods depending on internal optimizations, a list comprehension or join over iteration works well.
        # Given the constraint 'do not use any library functions other than those included with python',
        # we can implement it using string concatenation via join which is optimized but conceptually O(n).
        
        return ''.join(char for char in input_str if char != " ")

if __name__ == '__main__':
    sp = StringProcessor()
    
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    test_cases = [
        "Hello World",
        "  Python   Programming ",
        "",
        "No spaces here",
        "Multiple   Spaces   Inbetween"
    ]
    
    for test_input in test_cases:
        result = sp.remove_spaces(test_input)
        print(f'Input: "{test_input}" -> Output: "{result}"')