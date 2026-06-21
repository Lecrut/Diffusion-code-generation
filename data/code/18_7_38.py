def is_value_above_threshold(value, threshold=10):
    return value > threshold

if __name__ == '__main__':
    test_cases = [
        (5, 10),
        (15, 10),
        (20, 10),
        (10, 10),
        (-5, 0)
    ]
    
    for i, (value, threshold) in enumerate(test_cases):
        result = is_value_above_threshold(value, threshold)
        print(f"Test case {i+1}: is_value_above_threshold({value}, {threshold}) = {result}")