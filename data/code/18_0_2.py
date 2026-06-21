def find_middle_element(data_list):
    mid_index = len(data_list) // 2
    return data_list[mid_index]

if __name__ == '__main__':
    odd_length_list = [10, 20, 30, 40, 50]
    even_length_list = [5, 15, 25, 35, 45, 55]
    result_odd = find_middle_element(odd_length_list)
    result_even = find_middle_element(even_length_list)
    print(result_odd)
    print(result_even)