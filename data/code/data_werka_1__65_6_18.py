def get_element_at_index(data_list, index):
    if not isinstance(data_list, list):
        raise TypeError("data_list must be a list")
    if not isinstance(index, int):
        raise TypeError("index must be an integer")
    if index < 0 or index >= len(data_list):
        raise IndexError("Index out of bounds")
    return data_list[index]

if __name__ == '__main__':
    sample_data = [15, 25, 35, 45, 55, 65, 75]
    target_index = 3
    try:
        element = get_element_at_index(sample_data, target_index)
        print(element)
    except (TypeError, IndexError) as e:
        print(e)