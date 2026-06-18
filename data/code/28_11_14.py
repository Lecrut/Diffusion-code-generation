class ComparisonTool:
    def check_greater(self, value1, value2):
        """
        Compares two values using efficient built-in operators.
        
        Args:
            value1 (Any): First value to compare.
            value2 (Any): Second value to compare.
            
        Returns:
            bool: True if value1 > value2, False otherwise.
        """
        return value1 > value2

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    samples = [
        (45, 30),      # Integers
        ("apple", "banana"),  # Strings
        (3.14, 2.71),  # Floats
        ((1,), ()),     # Tuples with different lengths/contents
    ]

    tool = ComparisonTool()

    for i, vals in enumerate(samples):
        v1, v2 = vals
        result = tool.check_greater(v1, v2)
        print(f"Sample {i + 1}: compare {v1} and {v2}")
        print(f"is {v1} > {v2}? : {result}\n")