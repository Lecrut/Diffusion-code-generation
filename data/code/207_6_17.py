def find_largest(gen):
    try:
        largest = next(gen)
    except StopIteration:
        raise ValueError("Input generator cannot be empty")
    
    for item in gen:
        if item > largest:
            largest = item
    
    return largest

if __name__ == '__main__':
    test_cases = [
        ([1, 5, 2, 8, 3], 8),
        ([-10, -5, -20, -1], -1),
        ([5], 5),
        ([-100, -50, -10], -10),
        ([0, 0, 0], 0)
    ]
    
    for input_list, expected in test_cases:
        gen = iter(input_list)
        result = find_largest(gen)
        print(f"Input: {input_list}, Expected: {expected}, Result: {result}")