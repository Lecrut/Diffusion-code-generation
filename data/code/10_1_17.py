def get_first_element(sequence):
    start_index = 0
    target_item = sequence[start_index]
    return target_item

if __name__ == '__main__':
    test_data = ["zero", "one", "two"]
    first_value = get_first_element(test_data)
    print(first_value)