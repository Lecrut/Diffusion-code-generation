class ComparisonTool:
    """A utility class to compare two values efficiently."""

    @staticmethod
    def check_greater(val1, val2):
        """
        Compares two values and returns True if val1 is strictly greater than val2, False otherwise.
        
        Args:
            val1 (Any): The first value to compare.
            val2 (Any): The second value to compare.
            
        Returns:
            bool: True if val1 > val2, else False.
        """
        return val1 > val2

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input or files
    samples = [
        (50, 49),      # Expected: True
        (3.14, 3.15), # Expected: False
        ("apple", "banana"), # String comparison expected to be False ('a' < 'b')
        (-5, -6),      # Expected: True
    ]

    tool = ComparisonTool()
    
    for val_a, val_b in samples:
        result = tool.check_greater(val_a, val_b)
        print(f"Comparing {val_a} and {val_b}: {result}")