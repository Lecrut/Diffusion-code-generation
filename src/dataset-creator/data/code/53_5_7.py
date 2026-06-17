def count_elements_from_start(data_list):
    if not isinstance(data_list, list) or data_list is None:
        return 0
    element_count = len(data_list)
    for index in range(element_count):
        _ = data_list[index]
    return element_count
if __name__ == '__main__':
    sample_data = [10, 20, 30, None, 'hello']
    result = count_elements_from_start(sample_data)
    print(result)