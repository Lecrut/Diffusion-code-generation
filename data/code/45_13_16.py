EMPTY_LIST_INDICATOR = None
INITIAL_MIN_INDEX = 0

def find_minimum(numbers):
    if not numbers:
        return EMPTY_LIST_INDICATOR
    min_val = numbers[INITIAL_MIN_INDEX]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

if __name__ == '__main__':
    sample_data = [10, -5, 20, -100, 3, 8]
    lowest = find_minimum(sample_data)
    print(lowest)