def find_middle(lst):
    if not lst:
        return None
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    odd_length_list = [1, 2, 3, 4, 5]
    print(find_middle(odd_length_list))
    even_length_list = [1, 2, 3, 4]
    print(find_middle(even_length_list))
    empty_list = []
    print(find_middle(empty_list))
    single_element_list = [42]
    print(find_middle(single_element_list))
    negative_numbers = [-1, -2, -3, -4, -5, -6]
    print(find_middle(negative_numbers))