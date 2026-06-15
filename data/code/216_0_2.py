def find_middle_value(data):
    n = len(data)
    if n == 0:
        return None
    elif n % 2 == 1:
        middle_index = n // 2
        return data[middle_index]
    else:
        middle_right_index = n // 2
        middle_left_index = middle_right_index - 1
        return (data[middle_left_index] + data[middle_right_index]) / 2
if __name__ == '__main__':
    sample_list_odd = [1, 5, 3, 7, 9]
    sample_list_even = [10, 20, 30, 40]
    sample_list_empty = []
    result_odd = find_middle_value(sample_list_odd)
    result_even = find_middle_value(sample_list_even)
    result_empty = find_middle_value(sample_list_empty)
    print(f"Middle value of {sample_list_odd}: {result_odd}")
    print(f"Middle value of {sample_list_even}: {result_even}")
    print(f"Middle value of {sample_list_empty}: {result_empty}")