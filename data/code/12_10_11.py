def get_middle_element(lst):
    if not lst:
        return None
    return lst[len(lst) // 2]

if __name__ == '__main__':
    empty_list = []
    odd_list = [1, 3, 5, 7, 9]
    even_list = [1, 2, 3, 4, 5, 6]
    print(get_middle_element(empty_list))
    print(get_middle_element(odd_list))
    print(get_middle_element(even_list))