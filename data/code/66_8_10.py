def compare_adjacent(numbers):
    def is_valid_input(numbers):
        return isinstance(numbers, list) and all(isinstance(x, (int, float)) for x in numbers)

    if not is_valid_input(numbers):
        raise ValueError("Input must be a list of numbers")

    results = []
    n = len(numbers)
    if n < 2:
        return results

    for i in range(n - 1):
        results.append(numbers[i] <= numbers[i + 1])

    return results

if __name__ == '__main__':
    sample_array = [3, 5, 4, 8, 7, 9, 6]
    result = compare_adjacent(sample_array)
    print(result)