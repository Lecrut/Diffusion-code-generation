def compare_adjacent(numbers):
    def is_valid_input(lst):
        return isinstance(lst, list) and all(isinstance(x, (int, float)) for x in lst)

    if not is_valid_input(numbers):
        raise ValueError("Input must be a list of numbers.")

    result = []
    n = len(numbers)
    for i in range(n - 1):
        result.append(numbers[i] < numbers[i + 1])
    return result

if __name__ == '__main__':
    sample_array = [3, 1, 4, 1, 5, 9, 2, 6]
    result = compare_adjacent(sample_array)
    print(result)