FIRST_INDEX = 0
LAST_INDEX = -1
EMPTY_LIST_ERROR_MSG = "List must not be empty"

def get_endpoints(sequence):
    if len(sequence) == 0:
        raise ValueError(EMPTY_LIST_ERROR_MSG)
    first_val = sequence[FIRST_INDEX]
    last_val = sequence[LAST_INDEX]
    return first_val, last_val

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]
    start, end = get_endpoints(numbers)
    print(start, end)