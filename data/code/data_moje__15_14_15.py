SECOND_TO_LAST_INDEX = -2
MINIMUM_LENGTH = 2

def extract_second_to_last(item_list):
    if len(item_list) < MINIMUM_LENGTH:
        raise ValueError('List must contain at least two elements')
    return item_list[SECOND_TO_LAST_INDEX]

def validate_and_extract(item_list):
    error_messages = {0: 'List is empty', 1: 'List has only one element'}
    length = len(item_list)
    if length < MINIMUM_LENGTH:
        raise ValueError(error_messages.get(length, 'List too short'))
    return extract_second_to_last(item_list)
if __name__ == '__main__':
    test_cases = [[1, 2, 3, 4, 5], ['a', 'b', 'c', 'd'], [10, 20], ['x', 'y', 'z', 'w', 'v']]
    for test_list in test_cases:
        result = validate_and_extract(test_list)
        print(result)
    try:
        validate_and_extract([1])
    except ValueError as e:
        print(e)
    try:
        validate_and_extract([])
    except ValueError as e:
        print(e)