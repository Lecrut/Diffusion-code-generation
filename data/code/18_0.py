def find_middle_element(lst):
    if not lst:
        return None
    mid_index = len(lst) // 2
    return lst[mid_index]

if __name__ == '__main__':
    odd_list = [1, 2, 3, 4, 5]
    even_list = [1, 2, 3, 4]
    empty_list = []

    print(find_middle_element(odd_list))
    print(find_middle_element(even_list))
    print(find_middle_element(empty_list))