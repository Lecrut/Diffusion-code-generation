def check_equality(a: object, b: object) -> bool:
    """Check if two objects are equal using the built-in equality operator."""
    return a == b

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or files.
    print(check_equality([1, 2, 3], [1, 2, 3]))   # True
    print(check_equality("hello", "world"))        # False