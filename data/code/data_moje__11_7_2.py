def get_last_element(input_list):
    reversed_sequence = reversed(input_list)
    last_item = next(reversed_sequence)
    return last_item

if __name__ == '__main__':
    test_data = [10, 20, 30, 40, 50]
    output = get_last_element(test_data)
    print(output)