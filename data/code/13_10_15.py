def get_value_at_index(lst, index):
    if not isinstance(lst, list):
        raise TypeError("First argument must be a list")
    if not isinstance(index, int) or isinstance(index, bool):
        raise TypeError("Index must be an integer")
    if index < -len(lst) or index >= len(lst):
        raise ValueError(f"Index {index} is out of bounds for list of length {len(lst)}")
    return lst[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_value_at_index(sample_list, 0))
    print(get_value_at_index(sample_list, 2))
    print(get_value_at_index(sample_list, -1))
    try:
        get_value_at_index(sample_list, 5)
    except ValueError as e:
        print(e)
    try:
        get_value_at_index(sample_list, -6)
    except ValueError as e:
        print(e)