def get_middle_element(data):
    mid_index = len(data) // 2
    return data[mid_index]

if __name__ == '__main__':
    odd_length_list = [1, 3, 5, 7, 9]
    even_length_list = [2, 4, 6, 8]
    print(get_middle_element(odd_length_list))
    print(get_middle_element(even_length_list))