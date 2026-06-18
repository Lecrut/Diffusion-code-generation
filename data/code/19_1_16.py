def is_greater(a: any, b: any) -> bool:
    """Returns True if a > b, otherwise False."""
    return a > b

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input.
    result1 = is_greater(5, 3)       # Expected: True
    result2 = is_greater(2, 7)      # Expected: False
    result3 = is_greater('z', 'a')  # Expected: True (lexicographical comparison for strings)

    print(f"is_greater(5, 3) = {result1}")       # Prints: True
    print(f"is_greater(2, 7) = {result2}")      # Prints: False
    print(f"is_greater('z', 'a') = {result3}")   # Prints: True