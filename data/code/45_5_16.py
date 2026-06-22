EMPTY_LIST_MSG = "Input list must not be empty"
TYPE_CHECK_MSG = "Input must be a list"
INITIAL_MIN_INDEX = 0

def find_minimum(numbers):
    if not isinstance(numbers, list):
        raise TypeError(TYPE_CHECK_MSG)
    if len(numbers) == 0:
        raise ValueError(EMPTY_LIST_MSG)
    smallest = numbers[INITIAL_MIN_INDEX]
    for value in numbers:
        if value < smallest:
            smallest = value
    return smallest

if __name__ == '__main__':
    test_data = [42, -7, 100, 3, -1]
    computed_min = find_minimum(test_data)
    print(computed_min)