def get_value_at_index(lst, index):
    if index < 0:
        adjusted_index = len(lst) + index
        if adjusted_index < 0:
            raise ValueError("Index out of bounds")
        return lst[adjusted_index]
    if index >= len(lst):
        raise ValueError("Index out of bounds")
    return lst[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_value_at_index(sample_list, 2))
    print(get_value_at_index(sample_list, -1))
    print(get_value_at_index(sample_list, 4))