class Comparator:
    """A class designed to compare two objects."""

    @classmethod
    def are_unequal(cls, a, b):
        """
        Compare two arguments and return True if they are not equal, False otherwise.

        This method uses the standard equality operator (__eq__) inherited from object
        unless overridden by subclasses or specific types. It handles both immutable
        and mutable objects correctly based on their defined __eq__ behavior.

        Args:
            a (any): The first argument to compare.
            b (any): The second argument to compare.

        Returns:
            bool: True if 'a' is not equal to 'b', False otherwise.
        """
        return a != b

if __name__ == '__main__':
    # Hard-coded sample values for testing the are_unequal method
    
    # Test case 1: Integers (should be unequal)
    result_int = Comparator.are_unequal(5, 3)
    
    # Test case 2: Strings with different content (should be unequal)
    result_str_diff = Comparator.are_unequal("hello", "world")
    
    # Test case 3: Lists with same elements but different order (lists are not equal in Python)
    list_a = [1, 2]
    list_b = [2, 1]
    result_list_order = Comparator.are_unequal(list_a, list_b)
    
    # Test case 4: Same values (should be equal -> return False for unequal check)
    same_val = Comparator.are_unequal(5, 5)
    
    print(f"Integers 5 and 3 are unequal: {result_int}")      # True
    print(f"'hello' and 'world' are unequal: {result_str_diff}")   # True
    print(f"[1,2] and [2,1] are unequal: {result_list_order}")     # True (order matters in lists)
    print(f"5 and 5 are unequal: {same_val}")                   # False
    
    assert result_int == True, "Test case 1 failed."
    assert result_str_diff == True, "Test case 2 failed."
    assert result_list_order == True, "Test case 3 failed."
    assert same_val == False, "Test case 4 failed."
    
    print("All tests passed.")