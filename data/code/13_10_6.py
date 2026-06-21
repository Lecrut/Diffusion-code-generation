def get_value_at_index(lst, index):
    if not 0 <= index < len(lst):
        raise ValueError("Index is out of bounds")
    return lst[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    test_index = 2
    result = get_value_at_index(sample_list, test_index)
    print(result)
    try:
        get_value_at_index(sample_list, 10)
    except ValueError as e:
        print(e)