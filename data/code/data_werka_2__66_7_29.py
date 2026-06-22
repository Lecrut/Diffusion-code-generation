def is_ascending_sequence(numbers):
    ASCENDING_THRESHOLD = 0
    return [numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1)]

if __name__ == '__main__':
    SAMPLE_VALUES = [10, 20, 30, 40, 50]
    result = is_ascending_sequence(SAMPLE_VALUES)
    print(result)