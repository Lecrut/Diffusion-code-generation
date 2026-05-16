def find_middle_value(data):
    n = len(data)
    if n == 0:
        return None
    elif n % 2 == 1:
        middle_index = n // 2
        return data[middle_index]
    else:
        middle_index_1 = n // 2 - 1
        middle_index_2 = n // 2
        return (data[middle_index_1] + data[middle_index_2]) / 2
if __name__ == '__main__':
    sample_list = [1, 5, 2, 8, 3]
    middle = find_middle_value(sample_list)
    print(middle)
    sample_list_even = [10, 20, 30, 40]
    middle_even = find_middle_value(sample_list_even)
    print(middle_even)
    sample_list_odd = [1, 2, 3, 4, 5]
    middle_odd = find_middle_value(sample_list_odd)
    print(middle_odd)
    sample_list_single = [42]
    middle_single = find_middle_value(sample_list_single)
    print(middle_single)