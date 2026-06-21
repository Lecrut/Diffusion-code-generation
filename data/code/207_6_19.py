def find_largest(data):
    return max(data)

if __name__ == '__main__':
    test_cases = [
        ([1, 5, 2, 8, 3], 8),
        ([-10, -5, -20, -1], -1),
        ([5], 5),
        ([-100, -50, -200], -100),
        ([0, 0, 0], 0)
    ]
    for input_list, expected in test_cases:
        result = find_largest(input_list)
        print(f"Input: {input_list}, Expected: {expected}, Result: {result}")