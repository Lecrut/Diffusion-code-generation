from typing import Any

class ValueChecker:
    def __init__(self) -> None:
        """Initialize the ValueChecker instance."""
        pass

    def is_unequal(self, value1: Any, value2: Any) -> bool:
        """
        Determine if two provided values are unequal.

        Args:
            value1 (Any): The first value to compare.
            value2 (Any): The second value to compare.

        Returns:
            bool: True if the values are not equal, False otherwise.
        """
        return value1 != value2

if __name__ == '__main__':
    checker = ValueChecker()

    # Test case 1: Integers
    result_int = checker.is_unequal(5, 3)
    print(f"Integers (5 vs 3): {result_int}")  # Expected: True

    # Test case 2: Strings
    result_str = checker.is_unequal("hello", "world")
    print(f"Strings ('hello' vs 'world'): {result_str}")  # Expected: True

    # Test case 3: Same values (integers)
    same_int_result = checker.is_unequal(10, 10)
    print(f"Same Integers (10 vs 10): {same_int_result}")  # Expected: False

    # Test case 4: None and int
    result_none_int = checker.is_unequal(None, 5)
    print(f"Mixed Types (None vs 5): {result_none_int}")  # Expected: True

    # Test case 5: Floats with slight difference
    float_result = checker.is_unequal(1.0, 2.0)
    print(f"Floats (1.0 vs 2.0): {float_result}")  # Expected: True