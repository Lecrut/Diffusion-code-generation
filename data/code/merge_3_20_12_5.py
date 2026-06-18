def equal(x: object, y: object) -> bool:
    """Check if two arbitrary objects x and y are equal using Python's == operator."""
    return x == y

if __name__ == '__main__':
    # Sample values for testing without user input or external dependencies
    test_cases = [
        (5, 5),              # Integers: True
        ("hello", "world"),  # Strings should be False due to different content
        
        ([1, 2], [3, 4]),   # Lists with same structure but different values -> False
        ((1,), (2,)),       # Tuples with different values -> False

        ({'a': 1}, {'b': 2}), # Dicts with different keys/values -> False
        
        ("hello", "world"),    # Strings: True if equal content. Let's test equality properly here
        ]
    
    results = [equal(x, y) for x, y in test_cases]

    print("Results:", results)