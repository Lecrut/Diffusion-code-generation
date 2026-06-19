def get_first_item(data):
    return data[0]

if __name__ == '__main__':
    mixed_data = [True, 42, "world", {'key': 'value'}, (1, 2)]
    first_element = get_first_item(mixed_data)
    print(first_element)

    another_sample = ["start", 3.14, None]
    initial_value = get_first_item(another_sample)
    print(initial_value)