class Comparator:
    def check_equality(self, a, b):
        """
        Compares two arbitrary objects for equality using the built-in == operator.
        
        Parameters:
            self (Comparator): Instance of the Comparator class (required).
            a (any): First object to compare.
            b (any): Second object to compare.
            
        Returns:
            bool: True if a is equal to b, False otherwise.
        """
        return a == b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    cmp_obj = Comparator()

    # Test case 1: Integers
    result_ints = cmp_obj.check_equality(5, 5)
    
    # Test case 2: Strings
    result_strings = cmp_obj.check_equality("hello", "world")
    
    # Test case 3: Lists (mutable objects)
    list_a = [1, 2, 3]
    list_b = [4, 5, 6]
    result_lists_unequal = cmp_obj.check_equality(list_a, list_b)
    
    list_c = [1, 2, 3]
    list_d = [1, 2, 3]
    result_lists_equal = cmp_obj.check_equality(list_c, list_d)

    # Test case 4: Mixed types (should be False unless explicitly defined otherwise in a class)
    result_mixed = cmp_obj.check_equality(5.0, "5")

    print(f"Integers equal? {result_ints}")       # Expected: True
    print(f"Strings equal? {result_strings}")     # Expected: False
    print(f"Lists unequal? {result_lists_unequal}")  # Expected: True
    print(f"Lists equal? {result_lists_equal}")      # Expected: True
    print(f"Mixed types equal? {result_mixed}")   # Expected: False
    
    assert result_ints == True, "Integer comparison failed."
    assert result_strings == False, "String comparison failed."
    assert result_lists_unequal == True, "Unequal list comparison failed."
    assert result_lists_equal == True, "Equal list comparison failed."
    assert result_mixed == False, "Mixed type comparison failed."

    print("All tests passed successfully.")