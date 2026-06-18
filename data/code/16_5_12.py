def is_positive_generator(iterable):
    """Generator that yields True for every positive number in an iterable."""
    for item in iterable:
        if isinstance(item, (int, float)) and not isinstance(item, bool) and item > 0:
            yield True

if __name__ == '__main__':
    # Hard-coded sample values including positives, negatives, zeros, strings, booleans, and floats
    samples = [1, -5, 0.5, "hello", False, 3.2, None, 7]
    
    print("Testing positivity filter:")
    results = list(is_positive_generator(samples))
    print(f"Input: {samples}")
    print(f"Output (list of True for positives): {results}")