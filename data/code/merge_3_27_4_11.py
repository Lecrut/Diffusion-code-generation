def different_generator(a: int, b: int):
    """
    Generator function that yields True if two input numbers are different, 
    and False otherwise. It is memory efficient as it yields a single value immediately.
    
    Args:
        a (int): First number.
        b (int): Second number.
        
    Yields:
        bool: Result of the comparison between a and b.
    """
    result = a != b
    yield result

if __name__ == '__main__':
    # Sample values to test the generator function without user input or external dependencies
    sample_values = [(1, 2), (5, 5), (-3, -4), (0.5, 0.6)]

    for num_pair in sample_values:
        a, b = num_pair
        print(f"Comparing {a} and {b}: ", end="")
        
        # Create an iterator from the generator to consume it once
        gen_obj = different_generator(a, b)
        result_value = next(gen_obj) if hasattr(gen_obj, '__next__') else None
        
        print(result_value)