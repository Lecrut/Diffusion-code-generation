def get_value_at_index(lst, index):
    if index < 0 or index >= len(lst):
        raise ValueError("Index out of bounds")
    return lst[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    print(get_value_at_index(sample_list, 2))
    try:
        print(get_value_at_index(sample_list, 5))
    except ValueError as e:
        print(e)