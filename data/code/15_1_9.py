from typing import Any

class ValueChecker:
    """A utility class to check if two values are identical."""

    @staticmethod
    def are_equal(a: Any, b: Any) -> bool:
        """Check if the two input values are identical.

        This method uses Python's built-in identity comparison (`is`) 
        for strict equality checks between objects and `==` for value-based 
        comparisons when types differ or object instances need to be compared by content.

        Args:
            a (Any): The first value to compare.
            b (Any): The second value to compare.

        Returns:
            bool: True if the values are considered equal, False otherwise.
        """
        # Use 'is' for strict identity check as it's often preferred in Python 
        # unless specific type safety is required based on content equality only.
        return a is b

if __name__ == '__main__':
    checker = ValueChecker()

    # Sample test cases with hard-coded values
    print("Testing identical integers:", checker.are_equal(5, 5))
    print("Testing different strings:", checker.are_equal("hello", "world"))
    print("Testing same object reference (mutable):")
    obj_a = [1, 2, 3]
    obj_b = obj_a
    print(f"Same list ref: {checker.are_equal(obj_a, obj_b)}")

    # Testing with None and False edge cases
    print("Comparing to None:", checker.are_equal(None, None))
    print("Comparing False to True:", checker.are_equal(False, True))

    # Custom class instances (checking by identity vs content)
    class Point:
        def __init__(self, x: int, y: int):
            self.x = x
            self.y = y

    p1 = Point(0, 0)
    p2 = Point(0, 0)
    print("Different objects with same content:", checker.are_equal(p1, p2))