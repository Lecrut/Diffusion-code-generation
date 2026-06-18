def different_generator(a: int | float, b: int | float):
    """
    Generator function that yields a single boolean value indicating 
    whether two input numbers are different.
    
    Args:
        a (int or float): First number to compare.
        b (int or float): Second number to compare.
        
    Yields:
        bool: True if a != b, False otherwise.
    """
    yield a != b

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    results = list(different_generator(5, 10))
    print(f"Test case (5, 10): {results}")

    results2 = list(different_generator(3.5, 7.0))
    print(f"Test case (3.5, 7.0): {results2}")

    results3 = list(different_generator(-42, -42))
    print(f"Test case (-42, -42): {results3}")