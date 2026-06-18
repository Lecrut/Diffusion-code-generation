def check_equality(a: object = None, b: object = None) -> bool:
    """Check if two arbitrary Python objects are equal using the built-in equality operator."""
    return a == b

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or files
    result1 = check_equality({"key": "value"}, {"key": "value"})  # True (dicts with same content)
    result2 = check_equality([1, 2, 3], [4, 5, 6])              # False
    result3 = check_equality(42, 42.0)                           # False (int vs float)
    print(f"Dicts equal: {result1}, Lists differ: {not result2}, Int/Float differ: {not result3}")

# Time Complexity Analysis: O(1) for primitive types and small structures like int/float/string/tuple/list/dict/set if shallow comparison; 
# For complex nested objects, it is proportional to the number of elements compared in a deep equality check (O(n)), where n is the total size of smaller object structure.