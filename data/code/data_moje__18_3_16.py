def get_center_element(lst):
    center_index = len(lst) // 2
    if len(lst) % 2 == 1:
        return lst[center_index]
    else:
        return lst[center_index - 1], lst[center_index]

if __name__ == '__main__':
    odd_list = [1, 2, 3, 4, 5]
    even_list = [1, 2, 3, 4]
    print(get_center_element(odd_list))
    print(get_center_element(even_list))