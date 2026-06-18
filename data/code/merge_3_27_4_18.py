def different_numbers_generator(a: int | float, b: int | float):
    """
    Generator function that yields a single boolean value indicating 
    whether two input numbers are different.
    
    Args:
        a (int or float): First number.
        b (int or float): Second number.
        
    Yields:
        bool: True if a != b, False otherwise.
    """
    result = a != b
    yield result

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    samples = [
        (10, 20),      # Should yield True
        (5, 5),        # Should yield False
        (3.14, 3.14), # Should yield False
        (7, -7),       # Should yield True
        (0, 0)         # Should yield False
    ]

    for a, b in samples:
        print(f"Comparing {a} and {b}: ", end="")
        
        # Using next() to get the single yielded value from the generator
        result = next(different_numbers_generator(a, b))
        print(result)