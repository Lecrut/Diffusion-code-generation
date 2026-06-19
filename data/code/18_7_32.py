def is_greater_than_threshold(value, threshold=10):
    return value > threshold

if __name__ == '__main__':
    test_cases = [
        (5, 10),
        (15, 10),
        (20, 20),
        (0, -5)
    ]
    
    for value, threshold in test_cases:
        result = is_greater_than_threshold(value, threshold)
        print(f"is_greater_than_threshold({value}, {threshold}) = {result}")