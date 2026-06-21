def get_value_at_index(data, index):
    if index < 0 or index >= len(data):
        raise ValueError("Index out of bounds")
    return data[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    target_index = 2
    result = get_value_at_index(sample_list, target_index)
    print(result)
    try:
        get_value_at_index(sample_list, 10)
    except ValueError as e:
        print(e)