def get_value_at_index(lst, index):
    if index < 0 or index >= len(lst):
        raise ValueError("Index is out of bounds")
    return lst[index]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_index = 2
    try:
        result = get_value_at_index(sample_list, sample_index)
        print(result)
    except ValueError as e:
        print(e)