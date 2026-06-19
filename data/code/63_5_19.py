def fetch_initial_element(elements):
    return elements[0]

if __name__ == '__main__':
    test_data = [42, "world", 3.14159, {"key": "value"}, [1, 2, 3]]
    initial_value = fetch_initial_element(test_data)
    print(initial_value)

    another_test_data = ["start", 0, False]
    another_initial_value = fetch_initial_element(another_test_data)
    print(another_initial_value)

    single_item_list = ["only one"]
    single_initial_value = fetch_initial_element(single_item_list)
    print(single_initial_value)