def find_largest(data):
    if not data:
        raise ValueError("Input generator cannot be empty")
    largest = next(data)
    for item in data:
        if item > largest:
            largest = item
    return largest

if __name__ == '__main__':
    test_cases = [
        (iter([1, 5, 2, 8, 3]), 8),
        (iter([-10, -5, -20, -1]), -1),
        (iter([5]), 5),
        (iter([-100, -50, -10]), -10),
        (iter([0, 0, 0]), 0)
    ]
    for input_gen, expected in test_cases:
        result = find_largest(input_gen)
        print(f"Input: {list(input_gen)}, Largest: {result}")