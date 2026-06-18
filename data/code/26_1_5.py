class ComparisonUtils:
    @staticmethod
    def check_greater(val1, val2):
        """
        Checks if val1 is strictly greater than val2 using direct comparison operators.
        
        Args:
            val1 (any comparable type): The first value to compare.
            val2 (any comparable type): The second value to compare.
            
        Returns:
            bool: True if val1 > val2, False otherwise.
        """
        return val1 > val2

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    utils = ComparisonUtils()

    assert utils.check_greater(5, 3) is True
    assert utils.check_greater(3, 5) is False
    assert utils.check_greater("z", "a") is True
    assert utils.check_greater("a", "z") is False
    
    # Test with floats
    assert utils.check_greater(1.7890246, 1.789023) is True
    
    print("All sample checks passed successfully.")