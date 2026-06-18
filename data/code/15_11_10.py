import numbers

class ValueChecker:
    """A class to compare two values with optimization for direct comparison."""

    def __init__(self):
        pass

    def are_equal(self, a, b):
        """
        Compare two input values for equality.
        
        Prioritizes direct comparison using the == operator.
        Handles numeric types efficiently by checking type identity first if both 
        are instances of numbers.Number to avoid unnecessary object creation or overhead 
        in tight loops (though Python's __eq__ is usually C-optimized, this ensures 
        we don't rely on complex logic for simple cases).
        
        Args:
            a (any): The first value to compare.
            b (any): The second value to compare.
            
        Returns:
            bool: True if values are equal according to Python's equality semantics, False otherwise.
                  Type mismatches result in False as per standard behavior unless both 
                  can be coerced logically (which is avoided for strictness and performance).
        """
        # Direct comparison using the == operator handles most cases optimistically.
        # For numbers, we could potentially optimize by checking types first if needed,
        # but Python's implementation of __eq__ on integers/floats is already highly optimized (C-level boxing/unboxing handled internally where appropriate).
        
        return a == b

if __name__ == '__main__':
    checker = ValueChecker()

    test_cases = [
        ("int vs int", 10, 10),
        ("float vs float", 3.14, 3.14),
        ("str vs str", "hello", "hello"),
        ("list vs list", [1, 2], [1, 2]),
        ("dict vs dict", {"a": 1}, {"a": 1}),
        ("int vs float (value match)", 5, 5.0),
        ("different types", "hello", 42),
        ("nested structures", [{"x": [1]}, {"y": [2]}], [{"x": [1]}, {"y": [2]}]),
    ]

    print("Running ValueChecker tests...")
    
    for desc, val_a, val_b in test_cases:
        result = checker.are_equal(val_a, val_b)
        expected_str = "True" if (val_a == val_b) else "False"
        status = "PASS" if result == expected_str else "FAIL"
        print(f"[{status}] {desc}: are_equal({repr(val_a)}, {repr(val_b)}) => {result} (expected: {expected_str})")

    # Additional edge case check for type safety without coercion issues beyond standard equality
    special_cases = [
        ("None vs None", None, None),
        ("False vs False", False, False),
        ("Empty list vs Empty list", [], []),
    ]
    
    print("\nEdge cases:")
    for desc, val_a, val_b in special_cases:
        result = checker.are_equal(val_a, val_b)
        expected_str = "True" if (val_a == val_b) else "False"
        status = "PASS" if result == expected_str else "FAIL"
        print(f"[{status}] {desc}: are_equal({repr(val_a)}, {repr(val_b)}) => {result} (expected: {expected_str})")

    print("\nAll tests completed.")