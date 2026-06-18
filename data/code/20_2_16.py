class Comparator:
    def check_equality(self, a, b):
        """
        Compares two arbitrary objects for equality using the built-in == operator.
        
        Args:
            a (any): First object to compare.
            b (any): Second object to compare.
            
        Returns:
            bool: True if a is equal to b, False otherwise.
        """
        return a == b

if __name__ == '__main__':
    comp = Comparator()

    # Sample test cases with hard-coded values
    assert comp.check_equality(5, 5) is True
    assert comp.check_equality("hello", "world") is False
    assert comp.check_equality([1, 2], [3, 4]) is False
    assert comp.check_equality({"key": "value"}, {"key": "value"}) is True
    print("All equality checks passed.")