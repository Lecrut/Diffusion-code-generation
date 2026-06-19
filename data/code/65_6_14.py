def get_element_at_index(data_list, index):
    try:
        return data_list[index]
    except IndexError:
        raise ValueError("Index out of bounds")

if __name__ == '__main__':
    sample_data = [100, 200, 300, 400, 500, 600, 700]
    target_index = 3
    try:
        element = get_element_at_index(sample_data, target_index)
        print(element)
    except ValueError as e:
        print(e)