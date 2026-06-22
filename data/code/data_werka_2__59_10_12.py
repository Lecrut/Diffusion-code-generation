def find_middle_element(lst):
    if not lst:
        raise ValueError('The list is empty')
    middle_index = len(lst) // 2
    return lst[middle_index]

if __name__ == '__main__':
    odd_list = [7, 15, 23, 31, 39]
    even_list = [8, 16, 24, 32, 40, 48]
    print(find_middle_element(odd_list))
    print(find_middle_element(even_list))