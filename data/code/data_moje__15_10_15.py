MIN_LENGTH_REQUIRED = 2
ERROR_MSG_SHORT_LIST = "List must contain at least two elements"

def get_penultimate_element(sequence):
    if len(sequence) < MIN_LENGTH_REQUIRED:
        raise ValueError(ERROR_MSG_SHORT_LIST)
    return sequence[-MIN_LENGTH_REQUIRED]

if __name__ == '__main__':
    test_data = [100, 200, 300, 400, 500]
    result = get_penultimate_element(test_data)
    print(result)
    short_data = [42]
    try:
        get_penultimate_element(short_data)
    except ValueError as error:
        print(error)