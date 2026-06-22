def retrieve_initial_element(elements):
    return elements[0]

if __name__ == '__main__':
    EXAMPLE_LIST = [42, "answer", 3.14, {'key': 'value'}]
    initial_value = retrieve_initial_element(EXAMPLE_LIST)
    print(initial_value)

    ANOTHER_EXAMPLE = ["apple", False, 99]
    first_item = retrieve_initial_element(ANOTHER_EXAMPLE)
    print(first_item)

    SINGLE_ELEMENT_LIST = [True]
    sole_entry = retrieve_initial_element(SINGLE_ELEMENT_LIST)
    print(sole_entry)