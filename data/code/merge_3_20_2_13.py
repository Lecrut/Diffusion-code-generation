class Comparator:
    @staticmethod
    def check_equality(self, a, b):
        """
        Compares two arbitrary objects for equality using the built-in == operator.
        
        Args:
            self (any): Unused argument required by class method signature convention in this context.
            a (any): First object to compare.
            b (any): Second object to compare.
            
        Returns:
            bool: True if a is equal to b, False otherwise.
        """
        return a == b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    # Test with integers
    comp = Comparator()
    
    assert comp.check_equality(5, 5) is True
    assert comp.check_equality(5, 10) is False
    
    # Test with strings
    s1 = "hello"
    s2 = "world"
    result_str = comp.check_equality(s1, s2)
    print(f"String equality ('{s1}' == '{s2}'): {result_str}")  # Expected: False
    
    assert comp.check_equality("test", "test") is True
    
    # Test with lists (mutable objects)
    lst_a = [1, 2, 3]
    lst_b = [4, 5, 6]
    result_list = comp.check_equality(lst_a, lst_b)
    print(f"List equality ([1,2,3] == [4,5,6]): {result_list}")  # Expected: False
    
    assert comp.check_equality([1, 2], [1, 2]) is True
    
    # Test with mixed types (should be False unless explicitly defined otherwise)
    result_mixed = comp.check_equality(3.0, "3")
    print(f"Mixed type equality (3.0 == '3'): {result_mixed}")  # Expected: False
    
    assert result_mixed is False

    print("All tests passed.")