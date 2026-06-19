def fetch_element(data_list, index):
    if not isinstance(data_list, list) or not isinstance(index, int):
        return "Invalid input"
    try:
        return data_list[index]
    except IndexError:
        return None

if __name__ == '__main__':
    test_list = [10, 20, 30, 40, 50]
    valid_index = 2
    invalid_index = 7
    print(f"Element at index {valid_index}: {fetch_element(test_list, valid_index)}")
    print(f"Element at index {invalid_index}: {fetch_element(test_list, invalid_index)}")