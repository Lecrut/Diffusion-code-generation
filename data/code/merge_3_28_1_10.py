class ComparisonUtils:
    """A utility class providing comparison operations."""

    def check_if_greater(self, a, b):
        """
        Compares two arguments and returns True if 'a' is strictly greater than 'b', False otherwise.

        This method supports standard types (integers, floats) and any objects that implement the __gt__ magic method.
        
        Args:
            a: The first value to compare.
            b: The second value to compare against 'a'.

        Returns:
            bool: True if a > b is strictly true; False otherwise (including when types are incompatible).
        """
        try:
            return a > b
        except TypeError:
            # If the comparison raises an error due to type incompatibility, treat it as not greater.
            return False

if __name__ == '__main__':
    utils = ComparisonUtils()

    # Sample test cases without external input or files
    print("Integer 10 vs 5:", utils.check_if_greater(10, 5))       # Expected: True
    print("String 'z' vs 'a':", utils.check_if_greater('z', 'a'))   # Expected: True
    print("Float 3.14 vs 2.71:", utils.check_if_greater(3.14, 2.71)) # Expected: True

    print("\n--- Edge Cases ---")
    print("Equal values (5 vs 5):", utils.check_if_greater(5, 5))        # Expected: False
    print("Lesser value:", utils.check_if_greater(3, 4))                 # Expected: False
    
    # Testing with an object that supports comparison but is not strictly greater
    class CustomClass:
        def __init__(self, val):
            self.val = val

        def __gt__(self, other):
            return isinstance(other, int) and self.val > other
        
    obj1 = CustomClass(50)
    print("Custom object (val 50) vs 40:", utils.check_if_greater(obj1, 40)) # Expected: True

    try:
        invalid_obj = "I am not comparable"
        result = utils.check_if_greater(invalid_obj, int)
        print(f"Incompatible types comparison returned: {result}")
    except Exception as e:
        print("An unexpected error occurred:", type(e).__name__)