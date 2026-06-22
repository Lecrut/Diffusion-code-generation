def _validate_list_input(data):
    if not isinstance(data, list):
        raise TypeError("Input must be a list")
    if len(data) == 0:
        raise IndexError("Cannot retrieve head from an empty list")
    return True

def get_head(lst):
    _validate_list_input(lst)
    return lst[0]

if __name__ == '__main__':
    test_data = [99, 88, 77]
    result_value = get_head(test_data)
    print(result_value)