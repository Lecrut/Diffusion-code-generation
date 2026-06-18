class Comparator:
    @staticmethod
    def check_equality(self, a, b):
        """
        Compares two arbitrary objects for equality using the built-in == operator.
        
        Args:
            self (any): The first object (unused in static method but kept per signature).
            a (any): First value to compare.
            b (any): Second value to compare.
            
        Returns:
            bool: True if a is equal to b, False otherwise.
        """
        return a == b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    obj1 = "Hello"
    obj2 = "World"
    
    comp = Comparator()
    
    result_str_equal = comp.check_equality(obj1, obj2)  # Should be False
    print(f"'{obj1}' == '{obj2}': {result_str_equal}")

    obj3 = {"key": "value"}
    obj4 = {"key": "value"}
    
    result_dict_equal = comp.check_equality(obj3, obj4)  # Should be True
    
    class CustomClass:
        def __init__(self, val):
            self.val = val
        
        def __eq__(self, other):
            return isinstance(other, CustomClass) and self.val == other.val

    custom1 = CustomClass(5)
    custom2 = CustomClass(5)
    
    result_custom_equal = comp.check_equality(custom1, custom2)  # Should be True
    
    print(f"Custom class equality: {result_custom_equal}")