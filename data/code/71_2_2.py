def find_middle_value(data):
    n = len(data)
    if n == 0:
        return None
    else:
        middle_index = n // 2
        return data[middle_index]
if __name__ == '__main__':
    sample_list = [10, 5, 8, 3, 12]
    middle = find_middle_value(sample_list)
    print(middle)
    sample_list_even = [1, 2, 3, 4]
    middle_even = find_middle_value(sample_list_even)
    print(middle_even)
    sample_list_single = [42]
    middle_single = find_middle_value(sample_list_single)
    print(middle_single)
    sample_list_empty = []
    middle_empty = find_middle_value(sample_list_empty)
    print(middle_empty)