def find_middle_value(data):
    n = len(data)
    if n == 0:
        return None
    else:
        middle_index = n // 2
        return data[middle_index]
if __name__ == '__main__':
    sample_list = [10, 5, 20, 15, 30]
    middle = find_middle_value(sample_list)
    print(middle)
    sample_list_even = [1, 2, 3, 4, 5]
    middle_even = find_middle_value(sample_list_even)
    print(middle_even)
    sample_list_odd = [100, 50, 25]
    middle_odd = find_middle_value(sample_list_odd)
    print(middle_odd)
    sample_list_single = [42]
    middle_single = find_middle_value(sample_list_single)
    print(middle_single)