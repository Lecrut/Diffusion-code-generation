def check_difference(a: int | float, b: int | float) -> bool:
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
    test_cases = [
        (10, 20),      # Should be different -> True
        (5, 5),        # Same -> False
        (3.5, 4.5),    # Different floats -> True
        (-7, -7),      # Negative same -> False
        (0, 1)         # Zero and one -> True
    ]

    for num_a, num_b in test_cases:
        yield_value = check_difference(num_a, num_b)
        print(f"Numbers {num_a} and {num_b}: Yielded {yield_value}")