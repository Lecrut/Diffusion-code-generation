def find_middle_element(lst):
    n = len(lst)
    if n == 0:
        return None
    mid_index = n // 2
    if n % 2 == 1:
        return lst[mid_index]
    else:
        return (lst[mid_index - 1], lst[mid_index])

if __name__ == '__main__':
    odd_length_list = [1, 2, 3, 4, 5]
    even_length_list = [1, 2, 3, 4]
    empty_list = []
    single_element_list = [42]

    print(find_middle_element(odd_length_list))
    print(find_middle_element(even_length_list))
    print(find_middle_element(empty_list))
    print(find_middle_element(single_element_list))