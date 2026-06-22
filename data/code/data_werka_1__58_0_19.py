def retrieve_first_element(data_sequence):
    if not data_sequence:
        return None
    return data_sequence[0]

if __name__ == '__main__':
    test_list = [9, 18, 27, 36]
    first_item = retrieve_first_element(test_list)
    print(first_item)