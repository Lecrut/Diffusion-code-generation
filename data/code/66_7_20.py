def check_adjacent_ascending(numbers):
    return [numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1)]

if __name__ == '__main__':
    SAMPLE_VALUES = [5, 7, 6, 8, 9, 10]
    result = check_adjacent_ascending(SAMPLE_VALUES)
    print(result)