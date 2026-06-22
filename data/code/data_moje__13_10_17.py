def get_value_at_index(lst, index):
    if index < 0 or index >= len(lst):
        raise ValueError(f"Index {index} is out of bounds for list of length {len(lst)}")
    return lst[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    try:
        value = get_value_at_index(sample_list, 2)
        print(value)
    except ValueError as e:
        print(e)
    try:
        value = get_value_at_index(sample_list, 5)
        print(value)
    except ValueError as e:
        print(e)
    try:
        value = get_value_at_index(sample_list, -1)
        print(value)
    except ValueError as e:
        print(e)