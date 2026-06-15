def calculate_middle(data):
    n = len(data)
    middle_index = n // 2
    return data[middle_index]
if __name__ == '__main__':
    sorted_list = [2, 4, 6, 8, 10]
    middle_value = calculate_middle(sorted_list)
    print(middle_value)
    sorted_list_odd = [1, 3, 5, 7, 9]
    middle_value_odd = calculate_middle(sorted_list_odd)
    print(middle_value_odd)
    sorted_list_even = [2, 4, 6, 8]
    middle_value_even = calculate_middle(sorted_list_even)
    print(middle_value_even)