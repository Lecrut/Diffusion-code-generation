def fetch_element_by_index(data_list, position):
    if not isinstance(position, int) or position < 0 or position >= len(data_list):
        raise ValueError("Index out of bounds")
    return data_list[position]

if __name__ == '__main__':
    example_list = [7, 14, 21, 28, 35]
    target_index = 2
    try:
        result_element = fetch_element_by_index(example_list, target_index)
        print(result_element)
    except ValueError as e:
        print(e)