def is_non_empty(data):
    return bool(data)

def find_first_element(data):
    if not is_non_empty(data):
        return None
    return data[0]

if __name__ == '__main__':
    test_list = [1, 2, 3, 4, 5]
    first_value = find_first_element(test_list)
    print(first_value)