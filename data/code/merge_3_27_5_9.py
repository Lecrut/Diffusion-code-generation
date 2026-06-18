class ValueComparator:
    """A class designed to compare two values."""

    @staticmethod
    def are_unequal(arg1, arg2):
        """
        Compares two arguments and returns True if they are not equal, False otherwise.

        This method uses the built-in 'not' operator with equality check for clean implementation.
        
        Args:
            arg1 (any): The first value to compare.
            arg2 (any): The second value to compare.

        Returns:
            bool: True if arg1 is not equal to arg2, False otherwise.
        """
        return arg1 != arg2

if __name__ == '__main__':
    # Hard-coded sample values for testing the are_unequal method without user input.
    
    # Test case 1: Integers that are different
    result_int = ValueComparator.are_unequal(5, 10)
    print(f"Are 5 and 10 unequal? {result_int}")

    # Test case 2: Strings that are the same
    result_str_same = ValueComparator.are_unequal("hello", "hello")
    print(f"Are 'hello' and 'hello' unequal? {result_str_same}")

    # Test case 3: Mixed types (int vs float) which might compare equal or not depending on value, 
    # but here we use a clear mismatch.
    result_mixed = ValueComparator.are_unequal(42, "42")
    print(f"Are 42 and '42' unequal? {result_mixed}")

    # Test case 4: None vs Integer
    result_none_int = ValueComparator.are_unequal(None, 0)
    print(f"Are None and 0 unequal? {result_none_int}")