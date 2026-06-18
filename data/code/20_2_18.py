class Comparator:
    def check_equality(self, a, b):
        """
        Compares two arbitrary objects for equality using the built-in == operator.
        
        Args:
            a (object): The first object to compare.
            b (object): The second object to compare.
            
        Returns:
            bool: True if a and b are equal, False otherwise.
        """
        return a == b

if __name__ == '__main__':
    comp = Comparator()

    # Sample test cases with hard-coded values
    assert comp.check_equality(10, 10) is True
    
    assert comp.check_equality([1, 2], [1, 2]) is True
    
    assert comp.check_equality({"key": "value"}, {"key": "value"}) is True
    
    print("All sample equality checks passed.")