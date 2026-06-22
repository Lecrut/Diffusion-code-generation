def get_value_at_index(data, index):
    if index < 0 or index >= len(data):
        raise ValueError(f"Index {index} is out of bounds for list of size {len(data)}")
    return data[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    test_index = 2
    result = get_value_at_index(sample_list, test_index)
    print(result)