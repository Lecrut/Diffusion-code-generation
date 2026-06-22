def get_value_at_index(lst, index):
    if not isinstance(lst, list):
        raise TypeError("First argument must be a list")
    if not isinstance(index, int):
        raise TypeError("Index must be an integer")
    if index < 0 or index >= len(lst):
        raise ValueError("Index out of bounds")
    return lst[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_value_at_index(sample_list, 2))
    print(get_value_at_index(sample_list, 0))
    print(get_value_at_index(sample_list, 4))