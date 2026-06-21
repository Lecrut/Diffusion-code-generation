def find_middle_element(data):
    if not data:
        return None
    middle_index = len(data) // 2
    return data[middle_index]

if __name__ == '__main__':
    odd_length_list = [10, 20, 30, 40, 50]
    even_length_list = [1, 2, 3, 4, 5, 6]
    empty_list = []
    print(find_middle_element(odd_length_list))
    print(find_middle_element(even_length_list))
    print(find_middle_element(empty_list))