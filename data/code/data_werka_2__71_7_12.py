def get_middle_element(data):
    length = len(data)
    if length == 0:
        raise ValueError("List must not be empty")
    index_map = {True: length // 2, False: (length - 1) // 2}
    is_odd = length % 2 == 1
    target_index = index_map[is_odd]
    return data[target_index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    result = get_middle_element(sample_list)
    print(result)