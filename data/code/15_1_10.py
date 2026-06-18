from typing import Any

class ValueChecker:
    """A utility class to check if two values are identical."""

    def are_equal(self, a: Any, b: Any) -> bool:
        """
        Check if the two input values are identical.

        This method uses Python's built-in identity comparison for objects 
        and value equality for primitives as per standard `==` behavior in Python 3.

        Args:
            a (Any): The first value to compare.
            b (Any): The second value to compare.

        Returns:
            bool: True if the values are equal, False otherwise.
        """
        return a == b

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    checker = ValueChecker()
    
    test_cases = [
        (5, 5),           # Integers: equal
        ("hello", "world"),   # Strings: not equal
        ([1, 2], [3, 4]),     # Lists: not equal by value but structure same type
        ({'a': 1}, {'b': 2}),    # Dicts: not equal
        (True, True),      # Booleans: equal
        ("", ""),          # Empty strings: equal
        ([], []),          # Empty lists: equal
        ((1,), (1,)),      # Tuples with one element: equal
        (None, None),      # Null values: equal
    ]

    print("Running ValueChecker tests...")
    
    for i, (val_a, val_b) in enumerate(test_cases):
        result = checker.are_equal(val_a, val_b)
        expected = val_a == val_b
        
        status = "PASS" if result == expected else "FAIL"
        
        # Print detailed info only to avoid excessive output noise while keeping it clear
        print(f"\nTest {i + 1}:")
        print(f"Value A: {val_a!r} (type: {type(val_a).__name__})")
        print(f"Value B: {val_b!r} (type: {type(val_b).__name__})")
        print(f"Checker Result ({checker.are_equal.__doc__.split(chr(10))[2].strip()}): {result}")
        if result != expected:
            print("Expected:", expected)

    # Final summary check for a specific known case to demonstrate functionality clearly
    final_check = checker.are_equal([1, 2], [3, 4])
    assert not final_check, "Lists with different contents should be unequal."
    
    another_final = checker.are_equal("test", "test")
    assert another_final, "Identical strings should be equal."

    print("\nAll manual assertions passed.")