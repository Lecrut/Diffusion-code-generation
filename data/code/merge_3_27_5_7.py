class Comparator:
    """A class designed to compare two objects."""

    @staticmethod
    def are_unequal(obj1, obj2):
        """
        Compare two arguments and return True if they are not equal, False otherwise.

        This method uses the standard equality operator (__eq__) inherited from object
        or overridden by subclasses. It handles comparison of primitives (int, float, str)
        as well as custom objects that define __eq__.

        Args:
            obj1: The first argument to compare.
            obj2: The second argument to compare.

        Returns:
            bool: True if obj1 is not equal to obj2, False otherwise.
        """
        return not (obj1 == obj2)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    print(are_unequal(5, 5))          # Expected: False
    print(are_unequal("hello", "world"))  # Expected: True
    print(are_unequal([1, 2], [3, 4]))   # Expected: True
    
    class CustomClass:
        def __init__(self, value):
            self.value = value
        
        def __eq__(self, other):
            return isinstance(other, CustomClass) and self.value == other.value

    obj_a = CustomClass(10)
    obj_b = CustomClass(20)
    
    print(f"Custom objects unequal: {are_unequal(obj_a, obj_b)}")  # Expected: True
    
    class SameValueClass(CustomClass):
        pass
    
    same_obj = SameValueClass(10)
    print(f"Same value custom objects equal: {not are_unequal(obj_a, same_obj)}")  # Expected: True (so unequal returns False)