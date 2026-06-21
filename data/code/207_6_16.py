class MaxFinder:
    @staticmethod
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
        ([1, 5, 2, 8, 3], 8),
        ([-10, -5, -20, -1], -1),
        ([5], 5),
        ([-100, -50, -10], -10),
        ([0, 0, 0], 0)
    ]
    for input_list, expected in test_cases:
        generator = iter(input_list)
        result = MaxFinder.find_largest(generator)
        print(f"Input: {input_list}, Expected: {expected}, Result: {result}")