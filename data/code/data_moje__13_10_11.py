def get_value_at_index(data_list, index):
    if index < 0 or index >= len(data_list):
        raise ValueError("Index is out of bounds")
    return data_list[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    target_index = 2
    result = get_value_at_index(sample_list, target_index)
    print(result)