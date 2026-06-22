def get_value_by_index(lst, index):
    try:
        return lst[index]
    except IndexError:
        raise ValueError(f"Index {index} is out of bounds for list of length {len(lst)}")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    valid_index = 2
    invalid_index = 5

    result = get_value_by_index(sample_list, valid_index)
    print(result)

    try:
        get_value_by_index(sample_list, invalid_index)
    except ValueError:
        print("ValueError raised for invalid index")