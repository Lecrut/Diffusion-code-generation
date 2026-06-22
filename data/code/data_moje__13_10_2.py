def get_value_at_index(data, index):
    if index < 0 or index >= len(data):
        raise ValueError(f"Index {index} is out of bounds for list of length {len(data)}")
    return data[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    valid_index = 2
    invalid_index = 7
    print(get_value_at_index(sample_list, valid_index))
    try:
        print(get_value_at_index(sample_list, invalid_index))
    except ValueError as e:
        print(e)