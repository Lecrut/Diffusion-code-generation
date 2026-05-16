def find_middle_element(data):
    n = len(data)
    middle_index = n // 2
    return data[middle_index]
if __name__ == '__main__':
    sample_list_odd = [1, 2, 3, 4, 5]
    sample_list_even = [10, 20, 30, 40]
    sample_list_single = [99]
    result_odd = find_middle_element(sample_list_odd)
    result_even = find_middle_element(sample_list_even)
    result_single = find_middle_element(sample_list_single)
    print(f"Middle element of {sample_list_odd}: {result_odd}")
    print(f"Middle element of {sample_list_even}: {result_even}")
    print(f"Middle element of {sample_list_single}: {result_single}")