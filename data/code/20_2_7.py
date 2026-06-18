class Comparator:
    def check_equality(self, a, b):
        """
        Compares two arbitrary objects for equality using the built-in == operator.
        
        Args:
            self (object): The instance of the Comparator class.
            a: First object to compare.
            b: Second object to compare.
            
        Returns:
            bool: True if `a` is equal to `b`, False otherwise.
        """
        return a == b

if __name__ == '__main__':
    # Hard-coded sample values
    obj1 = {"key": "value"}
    obj2 = {"key": "value"}
    obj3 = [1, 2, 3]
    
    comparator = Comparator()
    
    result_1_eq_2 = comparator.check_equality(obj1, obj2)
    result_3_not_equal_obj1 = not comparator.check_equality(obj3, obj1)
    
    print(f"Is dict equal? {result_1_eq_2}")
    print(f"Are list and dict unequal? {result_3_not_equal_obj1}")