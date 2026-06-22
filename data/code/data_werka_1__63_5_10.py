def retrieve_first_element(elements):
    return elements[0]

if __name__ == '__main__':
    mixed_data = [42, "world", 3.14159, {'key': 'value'}, None]
    first_element = retrieve_first_element(mixed_data)
    print(first_element)

    another_sample = ["a", 1, 2.718, False]
    initial_value = retrieve_first_element(another_sample)
    print(initial_value)

    single_item_list = [True]
    sole_item = retrieve_first_element(single_item_list)
    print(sole_item)