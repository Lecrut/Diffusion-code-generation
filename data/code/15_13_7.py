def check_equality(a: object, b: object) -> bool:
    """Checks if two objects are equal using their built-in equality operator."""
    return a == b

if __name__ == '__main__':
    # Sample test cases with hard-coded values (no input required)
    print(check_equality(5, 5))          # True
    print(check_equality([1, 2], [3, 4]))        # False
    print(check_equality("hello", "world"))      # False
    print(check_equality(("a",), ("b",)))        # False