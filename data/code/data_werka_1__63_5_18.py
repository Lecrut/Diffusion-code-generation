def retrieve_initial_element(elements):
    return elements[0]

if __name__ == '__main__':
    example_data = ["banana", 42, 3.14159, {"key": "value"}]
    initial_value = retrieve_initial_element(example_data)
    print(initial_value)

    another_example = [True, None, "another"]
    first_entry = retrieve_initial_element(another_example)
    print(first_entry)