FIRST_ITEM_INDEX = 0

def _validate_list(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    if len(data) == 0:
        raise IndexError("list index out of range")
    return True

def retrieve_head(sequence):
    _validate_list(sequence)
    return sequence[FIRST_ITEM_INDEX]

if __name__ == '__main__':
    test_data = [42, 99, 15, 7]
    value = retrieve_head(test_data)
    print(value)