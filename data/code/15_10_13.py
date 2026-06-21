def get_penultimate_element(items):
    length = len(items)
    if length < 2:
        raise ValueError("List must contain at least two elements")
    return items[length - 2]

if __name__ == '__main__':
    numeric_sequence = [5, 12, 19, 26, 33]
    found_value = get_penultimate_element(numeric_sequence)
    print(found_value)
    try:
        get_penultimate_element([])
    except ValueError as error:
        print(error)
    single_item = [42]
    try:
        get_penultimate_element(single_item)
    except ValueError as error:
        print(error)