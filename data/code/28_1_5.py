class ComparisonUtils:
    """Utility class containing methods to perform comparisons."""

    @staticmethod
    def check_if_greater(arg1, arg2):
        """
        Compares two arguments and returns True if arg1 is greater than arg2, False otherwise.

        This method handles numeric types (int and float). For other comparable types, it attempts comparison directly.
        If the types are not compatible for direct comparison in Python 3 (e.g., int vs str), it raises a TypeError.

        Args:
            arg1: The first value to compare.
            arg2: The second value to compare.

        Returns:
            bool: True if arg1 > arg2, False otherwise.

        Raises:
            TypeError: If the arguments cannot be compared directly (e.g., different incompatible types).
        """
        return arg1 > arg2

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input or files
    
    result1 = ComparisonUtils.check_if_greater(10, 5)
    
    result2 = ComparisonUtils.check_if_greater("apple", "banana")
    
    result3 = ComparisonUtils.check_if_greater(8.9, 8.9)

    print(f"Is 10 greater than 5? {result1}")          # Expected: True
    print(f"Is 'apple' greater than 'banana'? {result2} (lexicographical comparison)")   # Expected: False ('a' < 'b')
    
    try:
        result4 = ComparisonUtils.check_if_greater(3, "three")
        print(f"Is 3 greater than 'three'? {result4}")
    except TypeError as e:
        print(f"Comparison between int and str failed as expected: {e}")   # Expected: TypeError
    
    try:
        result5 = ComparisonUtils.check_if_greater("hello", "world")
        is_hello_less_than_world = (result5 == False) or ("h" < "w")  # 'h' comes before 'w', so True > False? Wait. 
                             # Actually, we want to print the boolean of comparison directly if possible for consistency in other tests but here string compare logic:
    except TypeError as e2:
        pass

    # Corrected specific demo output line based on standard Python behavior where strings are compared lexicographically by default unless specified otherwise. 
    # "hello" < "world" is True (because 'h' < 'w'). So 10 > 5 -> T, string comp works in Py3.
    
    print(f"\nComparison summary:")
    print(f"{result1} | {result2}")