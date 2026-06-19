def get_first_item(data):
    if not data:
        return None
    return data[0]

if __name__ == '__main__':
    sample_list = [10, "hello", 3.14, True]
    first_value = get_first_item(sample_list)
    print(first_value)

    empty_list = []
    first_value_empty = get_first_item(empty_list)
    print(first_value_empty)

    single_element_list = ["single"]
    first_value_single = get_first_item(single_element_list)
    print(first_value_single)