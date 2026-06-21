def find_minimum(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty")
    MIN_VALUE = float('inf')
    minimum = MIN_VALUE
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum

if __name__ == '__main__':
    sample_values = [
        ([1, 5, 2, 8], 1),
        ([-10, -5, -20, -1], -20),
        ([3.14, 1.618, 2.718], 1.618),
        ([-5, 0, 5, -10], -10),
        ([7], 7)
    ]
    for input_list, expected in sample_values:
        result = find_minimum(input_list)
        print(f"Input: {input_list}, Expected: {expected}, Result: {result}")