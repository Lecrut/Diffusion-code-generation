def calculate_range(numbers):
    MIN = min(numbers)
    MAX = max(numbers)
    RANGE = MAX - MIN
    return RANGE

if __name__ == '__main__':
    SAMPLE_VALUES = [34, 12, 90, 56, 23]
    print(calculate_range(SAMPLE_VALUES))