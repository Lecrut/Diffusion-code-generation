class Comparator:
    @staticmethod
    def check_equality(self, a, b):
        """
        Compares two arbitrary objects for equality using the built-in `==` operator.
        
        Args:
            self (any): The instance of the class (not used in static method but required by Python convention).
            a (any): First object to compare.
            b (any): Second object to compare.
            
        Returns:
            bool: True if a is equal to b, False otherwise.
        """
        return a == b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    # Test with integers
    obj_int_1 = 5
    obj_int_2 = 5
    result_int = Comparator.check_equality(None, obj_int_1, obj_int_2)
    
    # Test with strings (case-sensitive equality)
    str_obj_1 = "hello"
    str_obj_2 = "HELLO"
    result_str_case = Comparator.check_equality(None, str_obj_1, str_obj_2)
    
    # Test case-insensitive string comparison using lower() method as a custom example of object behavior
    str_obj_3_lower = "hello".lower()
    str_obj_4_lower = "HELLO".lower()
    result_str_case_insensitive = Comparator.check_equality(None, str_obj_1.lower(), str_obj_2.lower())

    # Test with lists (equality based on content)
    list_obj_1 = [1, 2, 3]
    list_obj_2 = [4, 5, 6]
    result_list_diff = Comparator.check_equality(None, list_obj_1, list_obj_2)

    # Test with custom class instances containing attributes that might differ in order or case
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
        
        def to_tuple(self):
            return (self.x, self.y)
    
    point_1 = Point(5.0, 3.0)
    point_2 = Point(5.0, 3.0) # Same coordinates
    
    result_point_same_coords = Comparator.check_equality(None, point_1.to_tuple(), point_2.to_tuple())

    # Print results to verify functionality without external output files or prompts
    print(f"Integer equality check (expected: True): {result_int}")
    print(f"String case-sensitive check (expected: False): {result_str_case}")
    print(f"String case-insensitive check after lower() (expected: True): {result_str_case_insensitive}")
    print(f"Different list content check (expected: False): {result_list_diff}")
    print(f"Point coordinates equality via tuple conversion (expected: True): {result_point_same_coords}")