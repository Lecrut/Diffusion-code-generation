def _validate_bounds(length, index):
    if index < 0:
        return False
    if index >= length:
        return False
    return True

def get_value_at_index(data_list, index):
    if not isinstance(data_list, list):
        raise TypeError("Data must be a list")
    list_length = len(data_list)
    if not _validate_bounds(list_length, index):
        raise ValueError("Index is out of bounds")
    return data_list[index]

if __name__ == '__main__':
    records = [100, 200, 300, 400, 500]
    safe_index = 3
    unsafe_index = 6
    print(get_value_at_index(records, safe_index))
    try:
        print(get_value_at_index(records, unsafe_index))
    except ValueError as error:
        print(error)