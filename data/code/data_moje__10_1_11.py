def _validate_non_empty_list(data):
    if not isinstance(data, list):
        raise TypeError("Argument must be a list")
    if len(data) == 0:
        raise ValueError("List must not be empty")
    return True

def get_first_element(lst):
    _validate_non_empty_list(lst)
    first_index = 0
    return lst[first_index]

if __name__ == '__main__':
    sample_strings = ["hello", "world", "test"]
    result = get_first_element(sample_strings)
    print(result)