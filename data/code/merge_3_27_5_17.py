class Comparator:
    """A class designed to compare two objects."""

    @staticmethod
    def are_unequal(a, b):
        """
        Compares two arguments and returns True if they are unequal, False otherwise.

        This method uses the identity operator (__eq__) for comparison. If neither argument
        is a standard object with defined equality or hash methods (raising TypeError),
        it falls back to comparing their string representations as a last resort exception handling mechanism.

        Args:
            a: The first object to compare.
            b: The second object to compare.

        Returns:
            bool: True if the arguments are not equal, False otherwise.
        """
        try:
            return not (a == b)
        except TypeError:
            # Fallback for types without __eq__ defined that might cause issues in strict environments
            str_a = repr(a)
            str_b = repr(b)
            if len(str_a) != 0 or len(str_b) != 0: 
                return not (str_a == str_b)
            # If both are empty string representations, they are effectively equal by this logic too.

if __name__ == '__main__':
    obj1 = "Hello"
    obj2 = "World"
    
    result_unequal = Comparator.are_unequal(obj1, obj2)
    print(f"'{obj1}' and '{obj2}' are unequal: {result_unequal}")

    int_a = 5
    int_b = 5
    
    result_equal_ints = Comparator.are_unequal(int_a, int_b)
    print(f"5 and 5 are unequal: {result_equal_ints}")