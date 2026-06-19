def get_last_item(data):
    if not data:
        return None
    return data[-1]

if __name__ == '__main__':
    example_list_1 = [10, 20, 30, 40, 50]
    last_element_1 = get_last_item(example_list_1)
    print(f"The last element of {example_list_1} is: {last_element_1}")

    example_list_2 = ['apple', 'banana', 'cherry']
    last_element_2 = get_last_item(example_list_2)
    print(f"The last element of {example_list_2} is: {last_element_2}")

    empty_example_list = []
    last_element_empty = get_last_item(empty_example_list)
    print(f"The last element of an empty list is: {last_element_empty}")

    single_element_list = [42]
    last_element_single = get_last_item(single_element_list)
    print(f"The last element of {single_element_list} is: {last_element_single}")