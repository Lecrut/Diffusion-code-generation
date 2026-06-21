def get_first_element(data):
    if len(data) == 0:
        return None
    first_value = data[0]
    return first_value

if __name__ == '__main__':
    test_set = [42, 99, -5, 0]
    empty_set = []
    result_non_empty = get_first_element(test_set)
    result_empty = get_first_element(empty_set)
    print(result_non_empty)
    print(result_empty)